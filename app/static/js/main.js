productMainImage = document.getElementById('product-main-img')
productSubImages = document.querySelectorAll('.sub-image-list img')
quantity = document.querySelector('.product-quantity span')
modal = document.getElementById('pay-modal')

function setMain(id) {
  productMainImage.src = productSubImages[id].src
  productSubImages.forEach(element => {
    element.classList.remove('active')
  });
  productSubImages[id].classList.add('active')

}

function add(q) {
  old_q = quantity.innerText - 0 
  new_q = (old_q + q) >= 1  ? (old_q + q)  : 1
  quantity.innerText = new_q
}

function buy(id) {
  q = quantity.innerText - 0 
  window.location=`/payment?id=${id}&amount=${q}`;
}

function order() {
  modal.classList.add('show')
}