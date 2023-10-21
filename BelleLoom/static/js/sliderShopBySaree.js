const carouselSliderShopBySaree = document.querySelector(".image-slider-SAREE");
// console.log(carouselSliderShopBySaree)
firstImgShopBySaree = carouselSliderShopBySaree.querySelectorAll('img')[0];
arrowIconsShopBySaree = document.querySelectorAll('.wrapper-SAREE .pn-button-SAREE')


let isDragStartShopBySaree = false, prevShopBySareePageX, prevShopBySareeScrollLeft;

const showHideIconsShopBySaree = () => {
    // showing & hiding prev/ next icon according to craousel scroll left value
    let scrollWidth = carouselSliderShopBySaree.scrollWidth - carouselSliderShopBySaree.clientWidth; // getting max scrollable width
    arrowIconsShopBySaree[0].style.display = carouselSliderShopBySaree.scrollLeft == 0 ? "none" : "block";
    arrowIconsShopBySaree[1].style.display = carouselSliderShopBySaree.scrollLeft == scrollWidth ? "none" : "block";
}

arrowIconsShopBySaree.forEach(icon => {
    icon.addEventListener("click", () => {
        //if clicked icon is left, reduce width value from the carousel scroll left else add to it
        let firstImgWidth = firstImgShopBySaree.clientWidth + 14;   //getting first img width & adding 14 margin value
        carouselSliderShopBySaree.scrollLeft += icon.id == "left-SAREE" ? -firstImgWidth : firstImgWidth;
        setTimeout(() => showHideIconsShopBySaree() , 60);  //calling showShopBySareeHideIcons after 60ms
    })
});



const dragStartShopBySaree = (e) => {
    // updating global variables value on mouse down event
    isDragStartShopBySaree = true;
    prevShopBySareePageX = e.pageX || e.touches[0].pageX;
    prevShopBySareeScrollLeft = carouselSliderShopBySaree.scrollLeft;

}

const dragStopShopBySaree = () => {
    isDragStartShopBySaree = false;
    carouselSliderShopBySaree.classList.remove("draggingShopBySaree");
}

const draggingShopBySaree = (e) => {
    // console.log(e.pageX);
    // scrolling images/carousel to left according to the mouse pointer
    if(!isDragStartShopBySaree) return;
    e.preventDefault();
    carouselSliderShopBySaree.classList.add("draggingShopBySaree");
    let positionDiff = (e.pageX || e.touches[0].pageX) - prevShopBySareePageX
    carouselSliderShopBySaree.scrollLeft = prevShopBySareeScrollLeft - positionDiff;
    showHideIconsShopBySaree();
}

carouselSliderShopBySaree.addEventListener("mousedown",dragStartShopBySaree);
carouselSliderShopBySaree.addEventListener("touchstart",dragStartShopBySaree);

carouselSliderShopBySaree.addEventListener("mousemove",draggingShopBySaree);
carouselSliderShopBySaree.addEventListener("touchmove",draggingShopBySaree);

carouselSliderShopBySaree.addEventListener("mouseup",dragStopShopBySaree);
carouselSliderShopBySaree.addEventListener("touchend",dragStopShopBySaree);
carouselSliderShopBySaree.addEventListener("mouseleave",dragStopShopBySaree);