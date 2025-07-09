document.addEventListener("DOMContentLoaded", function () {
  const makeSelect = document.getElementById("id_make");
  const variantSelect = document.getElementById("id_variant");

  if (!makeSelect || !variantSelect) return;

  makeSelect.addEventListener("change", function () {
    const makeId = this.value;
    variantSelect.innerHTML = '<option value="">Select variant</option>';

    if (makeId) {
      fetch(`/variants/by-make/?make_id=${makeId}`)
        .then((response) => response.json())
        .then((data) => {
          data.forEach(function (variant) {
            const option = document.createElement("option");
            option.value = variant.id;
            option.textContent = variant.name;
            variantSelect.appendChild(option);
          });
        });
    }
  });
});
