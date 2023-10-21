const carouselSliderHairAccessory = document.querySelector(".image-slider-Hair-Accessory");
firstImgHairAccessory = carouselSliderHairAccessory.querySelectorAll('img')[0];
arrowIconsHairAccessory = document.querySelectorAll('.wrapper-Hair-Accessory .pn-button-Hair-Accessory')

let isDragStartHair = false, prevHairPageX, prevHairScrollLeft;

const showHairHideIcons = () => {
    // showing & hiding prev/ next icon according to craousel scroll left value
    let scrollWidth = carouselSliderHairAccessory.scrollWidth - carouselSliderHairAccessory.clientWidth; // getting max scrollable width
    arrowIconsHairAccessory[0].style.display = carouselSliderHairAccessory.scrollLeft == 0 ? "none" : "block";
    arrowIconsHairAccessory[1].style.display = carouselSliderHairAccessory.scrollLeft == scrollWidth ? "none" : "block";
}

arrowIconsHairAccessory.forEach(icon => {
    icon.addEventListener("click", () => {
        //if clicked icon is left, reduce width value from the carousel scroll left else add to it
        let firstImgWidth = firstImgHairAccessory.clientWidth + 14;   //getting first img width & adding 14 margin value
        carouselSliderHairAccessory.scrollLeft += icon.id == "leftHairAccessory" ? -firstImgWidth : firstImgWidth;
        setTimeout(() => showHairHideIcons() , 60);  //calling showHairHideIcons after 60ms
    })
});



const dragStartHair = (e) => {
    // updating global variables value on mouse down event
    isDragStartHair = true;
    prevHairPageX = e.pageX || e.touches[0].pageX;
    prevHairScrollLeft = carouselSliderHairAccessory.scrollLeft;
}

const dragStopHair = () => {
    isDragStartHair = false;
    carouselSliderHairAccessory.classList.remove("draggingHair");
}

const draggingHair = (e) => {
    // console.log(e.pageX);
    // scrolling images/carousel to left according to the mouse pointer
    if(!isDragStartHair) return;
    e.preventDefault();
    carouselSliderHairAccessory.classList.add("draggingHair");
    let positionDiff = (e.pageX || e.touches[0].pageX) - prevHairPageX
    carouselSliderHairAccessory.scrollLeft = prevHairScrollLeft - positionDiff;
    showHairHideIcons();
}

carouselSliderHairAccessory.addEventListener("mousedown",dragStartHair);
carouselSliderHairAccessory.addEventListener("touchstart",dragStartHair);

carouselSliderHairAccessory.addEventListener("mousemove",draggingHair);
carouselSliderHairAccessory.addEventListener("touchmove",draggingHair);

carouselSliderHairAccessory.addEventListener("mouseup",dragStopHair);
carouselSliderHairAccessory.addEventListener("touchend",dragStopHair);
carouselSliderHairAccessory.addEventListener("mouseleave",dragStopHair);