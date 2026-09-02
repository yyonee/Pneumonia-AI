// Scroll ke form
function goToForm() {
  document.getElementById("form-section").scrollIntoView({
    behavior: "smooth",
  });
}

// Scroll ke hasil (kalau ada hasil)
function goToResult() {
  const resultSection = document.getElementById("result-section");
  if (resultSection) {
    resultSection.scrollIntoView({
      behavior: "smooth",
    });
  }
}
function validateForm() {
  const requiredFields = document.querySelectorAll("[required]");

  for (let field of requiredFields) {
    if (!field.value) {
      alert(`Silakan isi ${field.previousElementSibling.innerText}`);
      field.focus();
      return false;
    }
  }

  // validasi radio
  const radios = ["sex", "tb", "crd", "diabetes", "cvd", "confusion", "anemia"];

  for (let name of radios) {
    if (!document.querySelector(`input[name="${name}"]:checked`)) {
      alert("Masih ada pilihan yang belum dipilih.");
      return false;
    }
  }

  // validasi select (INI YANG KAMU CARI)
  const selects = document.querySelectorAll("select");

  for (let select of selects) {
    if (select.value === "") {
      alert(`Silakan pilih ${select.previousElementSibling.innerText}`);
      select.focus();
      return false;
    }
  }

  return true;
}


