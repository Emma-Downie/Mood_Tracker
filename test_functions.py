import os
import pytest
import csv
from mood_tracker_functions import add_entry, remove_entry, add_score, add_emotions, mark_entry_complete, view_entries, complete_entry


@pytest.fixture
def temp_csv_file(tmpdir):
    csv_file_path = os.path.join(tmpdir, "test_entries.csv")
    yield csv_file_path

# Test add_entry function
def test_add_entry(temp_csv_file, monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: 'Test Entry')
    add_entry(temp_csv_file)
    
    with open(temp_csv_file, 'r') as f:
        reader = csv.reader(f)
        entries = list(reader)
    
    assert len(entries) == 1
    assert entries[0][0] == 'Test Entry'
    assert entries[0][1] == 'False'



# Test remove_entry function
def test_remove_entry(temp_csv_file, monkeypatch, capsys):
    with open(temp_csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Test Entry', 'False'])
    
    monkeypatch.setattr('builtins.input', lambda _: 'Test Entry')
    remove_entry(temp_csv_file)
    
    with open(temp_csv_file, 'r') as f:
        reader = csv.reader(f)
        entries = list(reader)
    
    assert len(entries) == 0

