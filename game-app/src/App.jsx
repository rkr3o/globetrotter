import { useEffect, useState } from "react";
import axios from "axios";
import Confetti from "react-confetti";

const API_URL = "http://localhost:8000/api/destinations";

function App() {
  const [question, setQuestion] = useState(null);
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [feedback, setFeedback] = useState("");
  const [funFact, setFunFact] = useState("");
  const [correctCount, setCorrectCount] = useState(0);
  const [wrongCount, setWrongCount] = useState(0);
  const [nextButtonText, setNextButtonText] = useState("🔄 Next Question");
  const [showConfetti, setShowConfetti] = useState(false);
  const [showSadFace, setShowSadFace] = useState(false);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchQuestion();
  }, []);

  const fetchQuestion = async () => {
    setLoading(true);
    setQuestion(null); // Clear previous question while loading a new one
    setSelectedAnswer(null);
    setFeedback("");
    setFunFact("");
    setShowConfetti(false);
    setShowSadFace(false);
    setNextButtonText("🔄 Next Question");

    const controller = new AbortController(); // Abort previous API calls
    const signal = controller.signal;

    try {
      const response = await axios.post(
        API_URL,
        {
          category: "travel",
          difficulty: "easy",
          user_id: "2344",
          action: "random_destination",
        },
        { signal }
      );

      setQuestion(response.data);
    } catch (error) {
      if (axios.isCancel(error)) {
        console.log("Request canceled:", error.message);
      } else {
        console.error("Error fetching question:", error);
      }
    } finally {
      setLoading(false);
    }

    return () => controller.abort(); // Cleanup on unmount
  };

  const handleAnswer = async (answer) => {
    if (!question || selectedAnswer !== null) return; // Prevent multiple submissions
    setSelectedAnswer(answer);

    try {
      const validationResponse = await axios.post(API_URL, {
        action: "validate_destination",
        clue_id: question.clue_id,
        clues: question.clues,
        user_answer: answer,
      });

      const { correct, message, fun_fact, correct_count, wrong_count, next_button } = validationResponse.data;

      setFeedback(message);
      setFunFact(fun_fact);
      setCorrectCount(correct_count);
      setWrongCount(wrong_count);
      setNextButtonText(next_button);

      if (correct) {
        setShowConfetti(true);
      } else {
        setShowSadFace(true);
      }
    } catch (error) {
      console.error("Error validating answer:", error);
      setFeedback("⚠️ Error validating answer. Please try again.");
    }
  };

  return (
    <div className="quiz-container">
      <h1>🌍 Travel Quiz</h1>
      {showConfetti && <Confetti />}
      {loading ? (
        <p>Loading question...</p>
      ) : question ? (
        <>
          <p><strong>Clues:</strong> {question.clues.join(" | ")}</p>
          <div className="options">
            {question.options.map((option) => (
              <button
                key={option}
                className={`option-btn ${selectedAnswer === option ? "selected" : ""}`}
                onClick={() => handleAnswer(option)}
                disabled={selectedAnswer !== null}
              >
                {option}
              </button>
            ))}
          </div>
          {feedback && <p className="feedback">{feedback}</p>}
          {showSadFace && <p className="sad-face">😢</p>}
          {funFact && <p className="fun-fact">💡 {funFact}</p>}
          <p>✅ Correct: {correctCount} | ❌ Wrong: {wrongCount}</p>
          <button className="next-btn" onClick={fetchQuestion}>{nextButtonText}</button>
        </>
      ) : (
        <p>Error loading question. Please try again.</p>
      )}
    </div>
  );
}

export default App;
