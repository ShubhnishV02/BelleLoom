const carouselSlider = document.querySelector(".image-slider");
firstImg = carouselSlider.querySelectorAll('img')[0];
arrowIcons = document.querySelectorAll('.wrapper .prev-next-button')
// console.log(carouselSlider);

let isDragStart = false, prevPageX, prevScrollLeft;

const showHideIcons = () => {
    // showing & hiding prev/ next icon according to craousel scroll left value
    let scrollWidth = carouselSlider.scrollWidth - carouselSlider.clientWidth; // getting max scrollable width
    arrowIcons[0].style.display = carouselSlider.scrollLeft == 0 ? "none" : "block";
    arrowIcons[1].style.display = carouselSlider.scrollLeft == scrollWidth ? "none" : "block";
}

arrowIcons.forEach(icon => {
    icon.addEventListener("click", () => {
        //if clicked icon is left, reduce width value from the carousel scroll left else add to it
        let firstImgWidth = firstImg.clientWidth + 14;   //getting first img width & adding 14 margin value
        carouselSlider.scrollLeft += icon.id == "left" ? -firstImgWidth : firstImgWidth;
        setTimeout(() => showHideIcons() , 60);  //calling showHideIcons after 60ms
    })
});



const dragStart = (e) => {
    // updating global variables value on mouse down event
    isDragStart = true;
    prevPageX = e.pageX || e.touches[0].pageX;
    prevScrollLeft = carouselSlider.scrollLeft;

}

const dragStop = () => {
    isDragStart = false;
    carouselSlider.classList.remove("dragging");
}

const dragging = (e) => {
    // console.log(e.pageX);
    // scrolling images/carousel to left according to the mouse pointer
    if(!isDragStart) return;
    e.preventDefault();
    carouselSlider.classList.add("dragging");
    let positionDiff = (e.pageX || e.touches[0].pageX)- prevPageX
    carouselSlider.scrollLeft = prevScrollLeft - positionDiff;
    showHideIcons();
}

carouselSlider.addEventListener("mousedown",dragStart);
carouselSlider.addEventListener("touchstart",dragStart);

carouselSlider.addEventListener("mousemove",dragging);
carouselSlider.addEventListener("touchmove",dragging);

carouselSlider.addEventListener("mouseup",dragStop);
carouselSlider.addEventListener("touchend",dragStop);
carouselSlider.addEventListener("mouseleave",dragStop);

