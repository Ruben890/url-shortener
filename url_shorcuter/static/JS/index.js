const btn_qr = document.querySelectorAll(".btn_qr");
const QR = document.querySelector(".QR");
const contents_qr = new QRCode(QR);
const btn_url = [...document.getElementsByClassName("btn_url")];
const a_url = document.getElementById("a_url");

btn_url.forEach((element) => {
  element.addEventListener("click", () => {
    window.open((location.href = element.value));
  });
});

btn_qr.forEach((element) => {
  element.addEventListener("click", () => {
    document.querySelector(".contens_qr").classList.toggle("active");
    contents_qr.makeCode(element.value);
  });
});

const none = () => {
  document.querySelector(".contens_qr").classList.toggle("active");
};
