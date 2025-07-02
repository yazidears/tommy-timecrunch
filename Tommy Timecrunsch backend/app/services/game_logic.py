import time
from ..models import GameState, db

def game_loop(app):
    with app.app_context():
        while True:
            game_state = GameState.query.first()
            if not game_state:
                game_state = GameState()
                db.session.add(game_state)
            
            game_state.tick += 1
            db.session.commit()

            print(f"Game tick: {game_state.tick}")

            # TODO: Implement game logic from plan.md
            # - Advance game state for all users
            # - Check deadlines, stress, finances, commitments
            # - Trigger random events and unexpected drama
            # - Inject new participants and incidents without user input

            time.sleep(10)
