// Create a new canvas to the browser size
function setup () {
  createCanvas(windowWidth, windowHeight);
}

// On window resize, update the canvas size
function windowResized () {
  resizeCanvas(windowWidth, windowHeight);
}

// Render loop that draws shapes with p5
function draw(){
  // For consistent sizing regardless of portrait/landscape
  const dim = Math.min(width, height);
  
  // Black background
  background(0);
  
  // Stroke only with a specific join style and thickness
  noFill();
  stroke(255);
  strokeCap(ROUND);
  strokeWeight(dim * 0.0075);

  // # of elements we wish to draw
  const count = 10;
  
  // Margin from edge of screen
  const margin = dim * 0.2;
  
  // The size with margin in consideration
  const innerWidth = (width - margin * 2);
  
  // Compute the diameter of each circle
  const diameter = innerWidth / (count - 1);

  for (let i = 0; i < count; i++) {
    // Get a 0..1 value across our loop
    const t = count <= 1 ? 0.5 : i / (count - 1);
    
    // The x position is linearly spaced across the inner width
    const x = lerp(margin, width - margin, t);
    
    // The y position is centred vertically
    const y = height * 0.125;
    
    ellipse(x, y, diameter, diameter, 0, PI * 2);
  }
  

  for (let i = 0; i < count; i++) {
    // Get a 0..1 value across our loop
    const t = count <= 1 ? 0.5 : i / (count - 1);
    
    // The x position is linearly spaced across the inner width
    const x = lerp(margin, width - margin, t);
    
    // The y position is centred vertically
    const y = height / 4;
    
    ellipse(x, y, diameter, diameter, 0, PI * 2);
  }

  for (let i = 0; i < count; i++) {
    // Get a 0..1 value across our loop
    const t = count <= 1 ? 0.5 : i / (count - 1);
    
    // The x position is linearly spaced across the inner width
    const x = lerp(margin, width - margin, t);
    
    // The y position is centred vertically
    const y = height * 0.375;
    
    ellipse(x, y, diameter, diameter, 0, PI * 2);
  }

  // Draw each circle
  for (let i = 0; i < count; i++) {
    // Get a 0..1 value across our loop
    const t = count <= 1 ? 0.5 : i / (count - 1);
    
    // The x position is linearly spaced across the inner width
    const x = lerp(margin, width - margin, t);
    
    // The y position is centred vertically
    const y = height / 2;
    
    ellipse(x, y, diameter, diameter, 0, PI * 2);
  }

  for (let i = 0; i < count; i++) {
    // Get a 0..1 value across our loop
    const t = count <= 1 ? 0.5 : i / (count - 1);
    
    // The x position is linearly spaced across the inner width
    const x = lerp(margin, width - margin, t);
    
    // The y position is centred vertically
    const y = height * 0.625;
    
    ellipse(x, y, diameter, diameter, 0, PI * 2);
  }

  for (let i = 0; i < count; i++) {
    // Get a 0..1 value across our loop
    const t = count <= 1 ? 0.5 : i / (count - 1);
    
    // The x position is linearly spaced across the inner width
    const x = lerp(margin, width - margin, t);
    
    // The y position is centred vertically
    const y = height * 0.75;
    
    ellipse(x, y, diameter, diameter, 0, PI * 2);
  }

  for (let i = 0; i < count; i++) {
    // Get a 0..1 value across our loop
    const t = count <= 1 ? 0.5 : i / (count - 1);
    
    // The x position is linearly spaced across the inner width
    const x = lerp(margin, width - margin, t);
    
    // The y position is centred vertically
    const y = height * 0.875;
    
    ellipse(x, y, diameter, diameter, 0, PI * 2);
  }
}