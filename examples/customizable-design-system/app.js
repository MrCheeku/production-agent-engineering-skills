const root = document.documentElement;
const toggle = document.querySelector("#theme-toggle");
const dialog = document.querySelector("#details-dialog");

toggle.addEventListener("click", () => {
  const next = root.dataset.theme === "dark" ? "light" : "dark";
  root.dataset.theme = next;
  toggle.setAttribute("aria-pressed", String(next === "dark"));
});

document.querySelector("#open-dialog").addEventListener("click", () => dialog.showModal());
