let currentIndex = 0;

const preview =
    document.getElementById("preview");

const counter =
    document.getElementById("counter");

function updatePhoto(){

    preview.src =
        photos[currentIndex];

    counter.innerText =
        `${currentIndex + 1} / ${photos.length}`;
}

document
.getElementById("nextBtn")
.addEventListener("click", ()=>{

    currentIndex++;

    if(currentIndex >= photos.length){
        currentIndex = 0;
    }

    updatePhoto();
});

document
.getElementById("prevBtn")
.addEventListener("click", ()=>{

    currentIndex--;

    if(currentIndex < 0){
        currentIndex = photos.length - 1;
    }

    updatePhoto();
});

let touchStartX = 0;
let touchEndX = 0;

preview.addEventListener(
    "touchstart",
    e=>{
        touchStartX =
            e.changedTouches[0].screenX;
    }
);

preview.addEventListener(
    "touchend",
    e=>{

        touchEndX =
            e.changedTouches[0].screenX;

        handleSwipe();
    }
);

function handleSwipe(){

    const distance =
        touchEndX - touchStartX;

    if(distance > 50){

        currentIndex--;

        if(currentIndex < 0){
            currentIndex = photos.length - 1;
        }

        updatePhoto();
    }

    if(distance < -50){

        currentIndex++;

        if(currentIndex >= photos.length){
            currentIndex = 0;
        }

        updatePhoto();
    }
}