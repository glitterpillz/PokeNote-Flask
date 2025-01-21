from app.models import db, JournalEntry, environment, SCHEMA
# from app.models.db import db, environment, SCHEMA
from datetime import datetime

def seed_journal_entries():
    # User 1's journal entries
    user1_entries = [
        JournalEntry(
            user_id=1,
            title="Day in the Mountains",
            content="Had a fantastic day hiking in the mountains!",
            accomplishments="Climbed the summit in under 2 hours.",
            timestamp=datetime(2025, 1, 3),
            photo=None,
            is_private=False
        ),
        JournalEntry(
            user_id=1,
            title="Hard day...",
            content="Work was exhausting today, but I managed to finish the report.",
            accomplishments="Completed the quarterly report on time.",
            timestamp=datetime(2025, 1, 2),
            photo=None,
            is_private=True
        ),
        JournalEntry(
            user_id=1,
            title="I'm a baker!",
            content="Rainy day at home, but I baked a cake!",
            accomplishments="Learned a new recipe.",
            timestamp=datetime(2025, 1, 1),
            photo=None,
            is_private=False
        ),
        JournalEntry(
            user_id=1,
            title="Reflections",
            content="Reflecting on my goals for the new year.",
            accomplishments="Created a vision board.",
            timestamp=datetime(2024, 12, 31),
            photo=None,
            is_private=True
        ),
        JournalEntry(
            user_id=1,
            title="Girl Dinner!",
            content="Had a lovely dinner with friends.",
            accomplishments="Reconnected with old friends.",
            timestamp=datetime(2024, 12, 30),
            photo=None,
            is_private=False
        )
    ]

    # User 2's journal entries
    user2_entries = [
        JournalEntry(
            user_id=2,
            title="Learning Code",
            content="Started learning a new programming language.",
            accomplishments="Completed the first tutorial for Python.",
            timestamp=datetime(2025, 1, 3),
            photo=None,
            is_private=False
        ),
        JournalEntry(
            user_id=2,
            title="Doomed",
            content="Feeling overwhelmed with work today.",
            accomplishments="Managed to prioritize tasks.",
            timestamp=datetime(2025, 1, 2),
            photo=None,
            is_private=True
        ),
        JournalEntry(
            user_id=2,
            title="Self Care Day",
            content="Went for a long walk in the park.",
            accomplishments="Walked 5 miles.",
            timestamp=datetime(2025, 1, 1),
            photo=None,
            is_private=False
        ),
        JournalEntry(
            user_id=2,
            title="Learning new skillz",
            content="Tried painting for the first time.",
            accomplishments="Completed a small landscape painting.",
            timestamp=datetime(2024, 12, 31),
            photo=None,
            is_private=False
        ),
        JournalEntry(
            user_id=2,
            title="Some more self care...",
            content="Late-night journaling to clear my mind.",
            accomplishments="Organized thoughts about future goals.",
            timestamp=datetime(2024, 12, 30),
            photo=None,
            is_private=True
        )
    ]

    # User 3's journal entries
    user3_entries = [
        JournalEntry(
            user_id=3,
            title="NEW PUPPY!!!",
            content="Adopted a new puppy today!",
            accomplishments="Welcomed a furry friend into my home.",
            timestamp=datetime(2025, 1, 3),
            photo=None,
            is_private=False
        ),
        JournalEntry(
            user_id=3,
            title="Meal Prep",
            content="Started meal prepping for the week.",
            accomplishments="Prepared meals for five days.",
            timestamp=datetime(2025, 1, 2),
            photo=None,
            is_private=True
        ),
        JournalEntry(
            user_id=3,
            title="Fam Movie Night!",
            content="Watched a great movie with family.",
            accomplishments="Spent quality time with loved ones.",
            timestamp=datetime(2025, 1, 1),
            photo=None,
            is_private=False
        ),
        JournalEntry(
            user_id=3,
            title="Scholarly Activities",
            content="Started reading a new book.",
            accomplishments="Finished two chapters of 'The Great Gatsby.'",
            timestamp=datetime(2024, 12, 31),
            photo=None,
            is_private=False
        ),
        JournalEntry(
            user_id=3,
            title="Vacayyyy",
            content="Planned a weekend getaway.",
            accomplishments="Booked tickets and accommodation.",
            timestamp=datetime(2024, 12, 30),
            photo=None,
            is_private=True
        )
    ]

    # Adding entries to the database
    all_entries = user1_entries + user2_entries + user3_entries
    for entry in all_entries:
        db.session.add(entry)

    db.session.commit()


def undo_journal_entries():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM journal_entries"))
        
    db.session.commit()