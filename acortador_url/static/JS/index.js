const btn_qr = document.querySelectorAll(".btn_qr");
const QR = document.querySelector(".QR");
const contents_qr = new QRCode(QR);

btn_qr.forEach((element) => {
  element.addEventListener("click", () => {
    document.querySelector(".contens_qr").classList.toggle("active");
    contents_qr.makeCode(element.value);
  });
});

const none = () => {
  document.querySelector(".contens_qr").classList.toggle("active");
};
