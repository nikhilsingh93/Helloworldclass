
var positions;

let tf="FACE";

function setup() {

  // setup camera capture
  var videoInput = createCapture();
  videoInput.size(400, 300);
  videoInput.position(0, 0);
  
  // setup canvas
  var cnv = createCanvas(400, 400);
  cnv.position(0, 0);

  // setup tracker
  ctracker = new clm.tracker();
  ctracker.init(pModel);
  ctracker.start(videoInput.elt);
  
  fill(255);

  tf=tf.split('');
  console.log(text);
}

let j=0;

function draw() {
  clear();
  
  push();
  textSize(72);
  textAlign(CENTER);
  text("FACE", width/2,height/2);
  pop();
  
  // get array of face marker positions [x, y] format
  positions = ctracker.getCurrentPosition();
  
  for (var i=0; i<positions.length; i++) {
    stroke(0);
    fill(0);
    text(tf[j],positions[i][0],positions[i][1]);
    j++;
    if(j>=text.length){
        j=0;
    }
  }
}
