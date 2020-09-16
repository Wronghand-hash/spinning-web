let card = document.querySelector("#card");
console.log(card);
card.addEventListener('mouseover', () => {
  document.body.style.backgroundImage = "{% static 'frontend.jpg' %}";
});
