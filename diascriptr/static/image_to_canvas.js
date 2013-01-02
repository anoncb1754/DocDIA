//Javascript code to put an image into the canvas

function putImageToCanvas(imgSrc)
{
	
	console.log("Starting...");
	var x = 0;
	var y = 0;

	var imageObj = new Image();

	imageObj.src = imgSrc;

	imageObj.onload = function()
	{
		var canvas = document.getElementById("display_page");
		var context = canvas.getContext('2d');
		context.drawImage(imageObj, x, y, imageObj.width, imageObj.height);
	};
};

//function for resizing the image into the canvas if image is larget than canvas


//function for zooming in to the canvas imageObj

//function for zooming out of the canvas


//function to fit image to canvas