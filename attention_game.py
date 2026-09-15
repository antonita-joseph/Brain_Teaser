import tkinter as tk
from tkinter import messagebox
import random
import time


class AttentionGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Letter & Number Attention Game")
        self.root.geometry("800x1000")
        self.root.resizable(False, False)

        # -----------------------------
        # Game configuration
        # -----------------------------
        self.total_rounds = 30
        self.current_round = 0
        self.score = 0

        self.vowels = {"A", "E", "I", "O", "U"}

        # Current question variables
        self.current_letter = ""
        self.current_number = 0
        self.current_target = ""

        # -----------------------------
        # TIME TRACKING VARIABLES
        # -----------------------------
        self.answer_start_time = 0.0
        self.reaction_times = []

        # Prevent multiple button clicks
        self.answer_locked = False

        # -----------------------------
        # Main title
        # -----------------------------
        self.title_label = tk.Label(
            root,
            text="ATTENTION TEST",
            font=("Arial", 26, "bold")
        )
        self.title_label.pack(pady=20)

        # -----------------------------
        # Instructions
        # -----------------------------
        self.instruction_label = tk.Label(
            root,
            text=(
                "LETTER:  Vowel = Left     Consonant = Right\n"
                "NUMBER:  Even = Left     Odd = Right"
            ),
            font=("Arial", 14)
        )
        self.instruction_label.pack(pady=10)

        # -----------------------------
        # Round information
        # -----------------------------
        self.round_label = tk.Label(
            root,
            text="Press START to begin",
            font=("Arial", 14, "bold")
        )
        self.round_label.pack(pady=15)

        # -----------------------------
        # Target: LETTER / NUMBER
        # -----------------------------
        self.target_label = tk.Label(
            root,
            text="",
            font=("Arial", 22, "bold")
        )
        self.target_label.pack(pady=10)

        # -----------------------------
        # Letter and number display
        # -----------------------------
        self.display_label = tk.Label(
            root,
            text="",
            font=("Arial", 48, "bold"),
            width=12,
            height=2,
            relief="ridge",
            borderwidth=4
        )
        self.display_label.pack(pady=20)

        # -----------------------------
        # Answer buttons
        # -----------------------------
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.button1 = tk.Button(
            self.button_frame,
            text="Left",
            font=("Arial", 24, "bold"),
            width=8,
            height=2,
            state="disabled",
            command=lambda: self.check_answer(1)
        )
        self.button1.grid(row=0, column=0, padx=20)

        self.button2 = tk.Button(
            self.button_frame,
            text="Right",
            font=("Arial", 24, "bold"),
            width=8,
            height=2,
            state="disabled",
            command=lambda: self.check_answer(2)
        )
        self.button2.grid(row=0, column=1, padx=20)

        # -----------------------------
        # Feedback
        # -----------------------------
        self.feedback_label = tk.Label(
            root,
            text="",
            font=("Arial", 15, "bold")
        )
        self.feedback_label.pack(pady=15)

        # -----------------------------
        # Score
        # -----------------------------
        self.score_label = tk.Label(
            root,
            text="Score: 0",
            font=("Arial", 13)
        )
        self.score_label.pack()

        # -----------------------------
        # Start button
        # -----------------------------
        self.start_button = tk.Button(
            root,
            text="START GAME",
            font=("Arial", 16, "bold"),
            width=15,
            command=self.start_game
        )
        self.start_button.pack(pady=20)

    # =============================================
    # Start / Restart game
    # =============================================
    def start_game(self):
        self.current_round = 0
        self.score = 0

        # Clear previous timing results
        self.reaction_times = []

        self.score_label.config(text="Score: 0")
        self.feedback_label.config(text="")
        self.start_button.config(state="disabled")

        self.button1.config(state="normal")
        self.button2.config(state="normal")

        self.next_question()

    # =============================================
    # Generate next question
    # =============================================
    def next_question(self):

        if self.current_round >= self.total_rounds:
            self.end_game()
            return

        self.answer_locked = False

        self.current_round += 1

        # Generate random letter A-Z 
        # The vowels are repeated to balance the weightage of occurences
        self.current_letter = random.choice(
            "AAAABCDEEEEFGHIIIIJKLMNOOOOPQRSTUUUUVWXYZ"
        )

        # Generate random number 1-9
        self.current_number = random.randint(1, 9)

        # Decide whether user should classify
        # LETTER or NUMBER
        self.current_target = random.choice(
            ["LETTER", "NUMBER"]
        )

        # Randomize presentation order
        if random.choice([True, False]):
            display_text = (
                f"{self.current_letter}     "
                f"{self.current_number}"
            )
        else:
            display_text = (
                f"{self.current_number}     "
                f"{self.current_letter}"
            )

        # Update GUI
        self.round_label.config(
            text=f"Round {self.current_round} / "
                 f"{self.total_rounds}"
        )

        self.target_label.config(
            text=f"CLASSIFY: {self.current_target}"
        )

        self.display_label.config(
            text=display_text
        )

        self.feedback_label.config(text="")

        self.button1.config(state="normal")
        self.button2.config(state="normal")

        # -----------------------------------------
        # START TIMER FOR THIS QUESTION
        # -----------------------------------------
        self.answer_start_time = time.perf_counter()

    # =============================================
    # Process answer
    # =============================================
    def check_answer(self, selected_answer):

        if self.answer_locked:
            return

        self.answer_locked = True

        # -----------------------------------------
        # STOP TIMER
        # -----------------------------------------
        answer_end_time = time.perf_counter()

        time_taken = (
            answer_end_time - self.answer_start_time
        )

        # Store response time
        self.reaction_times.append(time_taken)

        # Disable buttons temporarily
        self.button1.config(state="disabled")
        self.button2.config(state="disabled")

        # Determine correct answer
        if self.current_target == "LETTER":

            if self.current_letter in self.vowels:
                correct_answer = 1
            else:
                correct_answer = 2

        else:   # NUMBER

            if self.current_number % 2 == 0:
                correct_answer = 1
            else:
                correct_answer = 2

        # Check player's selection
        if selected_answer == correct_answer:
            self.score += 1

            self.feedback_label.config(
                text=f"Correct!   Time: {time_taken:.3f} seconds"
            )

        else:
            self.feedback_label.config(
                text=(
                    f"Incorrect! Correct answer: "
                    f"{correct_answer}   "
                    f"Time: {time_taken:.3f} seconds"
                )
            )

        self.score_label.config(
            text=f"Score: {self.score}"
        )

        # Show feedback for 500 ms before
        # presenting next question
        self.root.after(500, self.next_question)

    # =============================================
    # End game
    # =============================================
    def end_game(self):

        self.button1.config(state="disabled")
        self.button2.config(state="disabled")

        percentage = (
            self.score / self.total_rounds
        ) * 100

        # Calculate timing statistics
        if self.reaction_times:

            average_time = (
                sum(self.reaction_times)
                / len(self.reaction_times)
            )

            fastest_time = min(self.reaction_times)
            slowest_time = max(self.reaction_times)

        else:
            average_time = 0
            fastest_time = 0
            slowest_time = 0

        # Performance classification
        if percentage >= 90:
            performance = "Excellent"

        elif percentage >= 75:
            performance = "Good"

        elif percentage >= 60:
            performance = "Moderate"

        else:
            performance = "Needs Improvement"

        # Create detailed time report
        time_report = ""

        for index, reaction_time in enumerate(
            self.reaction_times, start=1
        ):
            time_report += (
                f"Question {index:02}: "
                f"{reaction_time:.3f} sec\n"
            )

        result = (
            f"TEST COMPLETED\n\n"
            f"Correct Answers: "
            f"{self.score}/{self.total_rounds}\n\n"
            f"Accuracy: {percentage:.1f}%\n"
            f"Performance: {performance}\n\n"
            f"Average Response Time: "
            f"{average_time:.3f} seconds\n"
            f"Fastest Response: "
            f"{fastest_time:.3f} seconds\n"
            f"Slowest Response: "
            f"{slowest_time:.3f} seconds"
        )

        self.target_label.config(
            text="TEST COMPLETED"
        )

        self.display_label.config(
            text=f"{percentage:.1f}%"
        )

        self.feedback_label.config(
            text=(
                f"Average response time: "
                f"{average_time:.3f} seconds"
            )
        )

        self.start_button.config(
            text="PLAY AGAIN",
            state="normal"
        )

        # Show results window
        self.show_results_window(
            result,
            time_report
        )

    # =============================================
    # Detailed results window
    # =============================================
    def show_results_window(
        self,
        summary,
        time_report
    ):

        result_window = tk.Toplevel(self.root)

        result_window.title("Test Results")
        result_window.geometry("500x600")

        heading = tk.Label(
            result_window,
            text="ATTENTION TEST RESULTS",
            font=("Arial", 20, "bold")
        )
        heading.pack(pady=15)

        summary_label = tk.Label(
            result_window,
            text=summary,
            font=("Arial", 13),
            justify="left"
        )
        summary_label.pack(pady=10)

        tk.Label(
            result_window,
            text="Response Time by Question",
            font=("Arial", 14, "bold")
        ).pack(pady=10)

        # Scrollable timing report
        text_box = tk.Text(
            result_window,
            height=14,
            width=40,
            font=("Courier New", 11)
        )

        text_box.pack(pady=5)

        text_box.insert(
            tk.END,
            time_report
        )

        text_box.config(
            state="disabled"
        )

        close_button = tk.Button(
            result_window,
            text="Close",
            font=("Arial", 12),
            width=12,
            command=result_window.destroy
        )

        close_button.pack(pady=15)


# =============================================
# Run application
# =============================================
if __name__ == "__main__":

    root = tk.Tk()

    game = AttentionGame(root)

    root.mainloop()
