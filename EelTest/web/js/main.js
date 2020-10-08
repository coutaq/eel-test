eel.expose(loadImage);
function readURL(input) {
    alert(input);
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#blah')
                .attr('src', e.target.result)
                .width(e.target.result.width)
                .height(e.target.result.height);
        };

        reader.readAsDataURL(input.files[0]);
    }
}

function loadImage(image){
    alert(image);
    $('#fileInput')
    .val = image;
}

