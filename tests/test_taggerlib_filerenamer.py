from darkseid.genericmetadata import GenericMetadata
from metrontagger.taggerlib.filerenamer import FileRenamer


def test_determine_name(fake_comic, fake_metadata):
    expected_result = "Aquaman v2 #001 (2011).cbz"

    renamer = FileRenamer(fake_metadata)
    new_file_name = renamer.determine_name(fake_comic)
    assert new_file_name == expected_result


def test_rename_file(fake_comic):
    md = GenericMetadata()
    md.series = "Batman"
    md.volume = "2"
    md.issue = "100"
    md.year = "2020"

    # Verify what the original name of the file is.
    assert fake_comic.name == "Aquaman v1 #001 (of 08) (1994).cbz"

    renamer = FileRenamer(md)
    renamed_file = renamer.rename_file(fake_comic)

    expected_result = f"{md.series} v{md.volume} #{md.issue} ({md.year}).cbz"
    assert expected_result == renamed_file.name
