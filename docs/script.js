const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

let snake = [{x: 200, y: 200}];
let food = {x: 100, y: 100};
let dx = 20;
let dy = 0;
let score = 0;

function drawGame() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw snake
    ctx.fillStyle = "green";
    snake.forEach(part => {
        ctx.fillRect(part.x, part.y, 18, 18);
    });

    // Draw food
    ctx.fillStyle = "red";
    ctx.fillRect(food.x, food.y, 18, 18);

    moveSnake();
    checkFood();

    setTimeout(drawGame, 120);
}

function moveSnake() {
    const head = {
        x: snake[0].x + dx,
        y: snake[0].y + dy
    };

    snake.unshift(head);
    snake.pop();

    // wall collision
    if (
        head.x < 0 ||
        head.x >= canvas.width ||
        head.y < 0 ||
        head.y >= canvas.height
    ) {
        alert("Game Over! Score: " + score);
        location.reload();
    }
}

function checkFood() {
    if (
        snake[0].x === food.x &&
        snake[0].y === food.y
    ) {
        snake.push({});
        score++;

        food = {
            x: Math.floor(Math.random() * 20) * 20,
            y: Math.floor(Math.random() * 20) * 20
        };
    }
}

document.addEventListener("keydown", event => {
    if (event.key === "ArrowUp" && dy === 0) {
        dx = 0;
        dy = -20;
    }
    if (event.key === "ArrowDown" && dy === 0) {
        dx = 0;
        dy = 20;
    }
    if (event.key === "ArrowLeft" && dx === 0) {
        dx = -20;
        dy = 0;
    }
    if (event.key === "ArrowRight" && dx === 0) {
        dx = 20;
        dy = 0;
    }
});

drawGame();
