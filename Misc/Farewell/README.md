# Farewell 

## The Challenge 

![Alt text](images/image.png)

## The Patterns

### Script to generate patterns

```javascript
let gridSize = 4;
let squareSize;
let grid = [];

function setup() {
  createCanvas(400, 400);
  squareSize = width / gridSize;

  // Initialize the grid with empty squares
  for (let i = 0; i < gridSize; i++) {
    grid[i] = [];
    for (let j = 0; j < gridSize; j++) {
      grid[i][j] = 0; // 0 represents an empty square
    }
  }
  
  // Create a download button
  downloadButton = createButton('Download Screenshot');
  downloadButton.position(10, height + 10);
  downloadButton.mousePressed(downloadScreenshot);
}

function draw() {
  background(220);

  // Draw the grid
  for (let i = 0; i < gridSize; i++) {
    for (let j = 0; j < gridSize; j++) {
      if (grid[i][j] === 1) {
        fill(0); // Solid black
      } else {
        fill(255); // Empty square
      }
      rect(i * squareSize, j * squareSize, squareSize, squareSize);
    }
  }
}

function mousePressed() {
  // Toggle the state of the square that was clicked
  let col = floor(mouseX / squareSize);
  let row = floor(mouseY / squareSize);

  if (col >= 0 && col < gridSize && row >= 0 && row < gridSize) {
    grid[col][row] = 1 - grid[col][row]; // Toggle between 0 and 1
  }
}

function downloadScreenshot() {
  // Create an off-screen graphics buffer to capture the screenshot
  let buffer = createGraphics(width, height);
  buffer.background(220);

  // Draw the grid on the buffer
  for (let i = 0; i < gridSize; i++) {
    for (let j = 0; j < gridSize; j++) {
      if (grid[i][j] === 1) {
        buffer.fill(0); // Solid black
      } else {
        buffer.fill(255); // Empty square
      }
      buffer.rect(i * squareSize, j * squareSize, squareSize, squareSize);
    }
  }

  // Save the buffer as an image file
  buffer.save("screenshot.png");
}

```

![Alt text](patterns/screenshot.png)

![Alt text](patterns/screenshot(1).png)

![Alt text](patterns/screenshot(2).png)

![Alt text](patterns/screenshot(3).png)

![Alt text](patterns/screenshot(4).png)

![Alt text](patterns/screenshot(5).png)

![Alt text](patterns/screenshot(6).png)

![Alt text](patterns/screenshot(7).png)

![Alt text](patterns/screenshot(8).png)
