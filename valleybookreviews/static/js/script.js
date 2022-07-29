/**
 * This will hide the sidebar by changing the display to 'none'.
 * @param {string} sideBarElement
 */
const hideSideBar = (sideBarElement) => {
  sideBarElement.classList.remove("d-flex");
  sideBarElement.classList.add("d-none");
};

/**
 * This will show the sidebar by changing the display to 'flex'.
 * @param {string} sideBarElement
 */
const showSideBar = (sideBarElement) => {
  sideBarElement.classList.remove("d-none");
  sideBarElement.classList.add("d-flex");
};

/**
 * If the sidebar is showing this will hide it and visa-versa if the sidebar is hiding, it will show it.
 * @param {string} sideBar
 */
const hamburgerMenu = (sideBar) => {
  const sideBarOn = sideBar.classList.contains("d-flex");
  if (sideBarOn) {
    hideSideBar(sideBar);
  } else {
    showSideBar(sideBar);
  }
};

/**
 * This will add an event listener to the hamburger icon when clicked.
 */
const hamburgerSelector = document.querySelector("#hamburgerMenuSelector");
hamburgerSelector.addEventListener("click", () => {
  const sideBarMenu = document.querySelector("#sideBar");
  hamburgerMenu(sideBarMenu);
});
