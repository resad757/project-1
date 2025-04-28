function MainComponent() {
    const [snake, setSnake] = React.useState([[0, 0]]);
const [food, setFood] = React.useState([5, 5]);
const [direction, setDirection] = React.useState("right");
const [gameOver, setGameOver] = React.useState(false);
const [score, setScore] = React.useState(0);
const [highScore, setHighScore] = React.useState(0);

React.useEffect(() => {
    const savedHighScore = localStorage.getItem('snakeHighScore');
if (savedHighScore) {
    setHighScore(parseInt(savedHighScore));
}
}, []);

React.useEffect(() => {
    const handleKeyPress = (e) => {
    switch (e.key) {
    case "ArrowUp":
if (direction !== "down") setDirection("up");
break;
case "ArrowDown":
if (direction !== "up") setDirection("down");
break;
case "ArrowLeft":
if (direction !== "right") setDirection("left");
break;
case "ArrowRight":
if (direction !== "left") setDirection("right");
break;
}
};

window.addEventListener("keydown", handleKeyPress);
return () => window.removeEventListener("keydown", handleKeyPress);
}, [direction]);

React.useEffect(() => {
if (gameOver) {
if (score > highScore) {
setHighScore(score);
localStorage.setItem('snakeHighScore', score.toString());
}
return;
}

const moveSnake = () => {
const newSnake = [...snake];
const head = [...newSnake[0]];

switch (direction) {
    case "up":
head[1] -= 1;
break;
case "down":
head[1] += 1;
break;
case "left":
head[0] -= 1;
break;
case "right":
head[0] += 1;
break;
}

if (head[0] < 0 || head[0] > 19 || head[1] < 0 || head[1] > 19) {
setGameOver(true);
return;
}

if (newSnake.some((segment) => segment[0] === head[0] && segment[1] === head[1])) {
setGameOver(true);
return;
}

newSnake.unshift(head);

if (head[0] === food[0] && head[1] === food[1]) {
setScore(score + 1);
setFood([
    Math.floor(Math.random() * 20),
    Math.floor(Math.random() * 20),
]);
} else {
newSnake.pop();
}

setSnake(newSnake);
};

const gameInterval = setInterval(moveSnake, 150);
return () => clearInterval(gameInterval);
}, [snake, direction, food, gameOver, score, highScore]);

const resetGame = () => {
    setSnake([[0, 0]]);
setFood([5, 5]);
setDirection("right");
setGameOver(false);
setScore(0);
};

return (
    <div
    style={{
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    padding: "20px",
    fontFamily: "Arial, sans-serif",
    minHeight: "100vh",
    background: "linear-gradient(135deg, #1e3c72 0%, #2a5298 100%)",
    color: "white"
    }}
    >
    <h1 style={{
    fontSize: "2.5rem",
    marginBottom: "20px",
    textShadow: "2px 2px 4px rgba(0,0,0,0.3)"
    }}>
    İlan Oyunu
    </h1>

    <div style={{
    display: "flex",
    gap: "20px",
    marginBottom: "20px"
    }}>
    <div style={{
    padding: "10px 20px",
    background: "rgba(255,255,255,0.1)",
    borderRadius: "10px",
    backdropFilter: "blur(5px)"
    }}>
    Xal: {score}
    </div>
    <div style={{
    padding: "10px 20px",
    background: "rgba(255,255,255,0.1)",
    borderRadius: "10px",
    backdropFilter: "blur(5px)"
    }}>
    Ən Yüksək Xal: {highScore}
    </div>
    </div>

    <div
    style={{
    position: "relative",
    width: "400px",
    height: "400px",
    border: "3px solid rgba(255,255,255,0.2)",
    borderRadius: "10px",
    backgroundColor: "rgba(0,0,0,0.2)",
    backdropFilter: "blur(5px)",
    boxShadow: "0 0 20px rgba(0,0,0,0.3)"
    }}
    >
    {snake.map((segment, index) => (
    <div
    key={index}
    style={{
    position: "absolute",
    width: "20px",
    height: "20px",
    backgroundColor: index === 0 ? "#4ade80" : "#22c55e",
    borderRadius: "5px",
    left: `${segment[0] * 20}px`,
    top: `${segment[1] * 20}px`,
    transition: "all 0.1s linear",
    boxShadow: index === 0 ? "0 0 10px rgba(74, 222, 128, 0.5)" : "none"
    }}
    />
))}
<div
style={{
    position: "absolute",
    width: "20px",
    height: "20px",
    backgroundColor: "#ef4444",
    borderRadius: "50%",
    left: `${food[0] * 20}px`,
top: `${food[1] * 20}px`,
boxShadow: "0 0 10px rgba(239, 68, 68, 0.5)"
}}
/>
</div>

  {gameOver && (
      <div style={{
      position: "absolute",
      top: "50%",
      left: "50%",
      transform: "translate(-50%, -50%)",
      background: "rgba(0,0,0,0.85)",
      padding: "30px",
      borderRadius: "15px",
      textAlign: "center",
      backdropFilter: "blur(10px)",
      animation: "fadeIn 0.3s ease-out"
      }}>
      <div style={{
      fontSize: "2rem",
      color: "#ef4444",
      marginBottom: "20px",
      textShadow: "2px 2px 4px rgba(0,0,0,0.3)"
      }}>
      Oyun Bitdi!
      </div>
      <div style={{ marginBottom: "20px" }}>
      Son Xal: {score}
      {score === highScore && score > 0 && (
      <div style={{ color: "#4ade80", marginTop: "10px" }}>
      Yeni Rekord! 🎉
      </div>
  )}
  </div>
    <button
onClick={resetGame}
style={{
    padding: "12px 24px",
    fontSize: "1.1rem",
    backgroundColor: "#4ade80",
    color: "white",
    border: "none",
    borderRadius: "8px",
    cursor: "pointer",
    transition: "all 0.2s ease",
    boxShadow: "0 4px 6px rgba(0,0,0,0.1)"
}}
      >
      Yenidən Başla
              </button>
                </div>
)}

<div
style={{
    marginTop: "20px",
    textAlign: "center",
    padding: "15px",
    background: "rgba(255,255,255,0.1)",
    borderRadius: "10px",
    backdropFilter: "blur(5px)",
    lineHeight: "1.6"
}}
      >
      İlanı idarə etmək üçün ox düymələrindən istifadə edin.
                                                       <br />
                                                       Qırmızı nöqtələri toplayaraq böyüyün.
                                                                                    <br />
                                                                                    Divarlara və ya özünüzə toxunmamağa diqqət edin!
</div>
  </div>
);
}

<style jsx global>{`
@keyframes fadeIn {
from {
    opacity: 0;
transform: translate(-50%, -40%);
}
to {
    opacity: 1;
transform: translate(-50%, -50%);
}
}
`}</style>