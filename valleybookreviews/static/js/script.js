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
 * This will hide the account menu bar.
 * @param {string} accountMenuElement
 */
const hideAccountMenu = (accountMenuElement) => {
  accountMenuElement.classList.remove("d-block");
  accountMenuElement.classList.add("d-none");
};

/**
 * This will show the account menu bar.
 * @param {string} accountMenuElement
 */
const showAccountMenu = (accountMenuElement) => {
  accountMenuElement.classList.remove("d-none");
  accountMenuElement.classList.add("d-block");
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
 * If the My Account menu is showing this will hide it and visa-versa if the menu is hiding, it will show it.
 * @param {string} accountMenu
 */
const myAccountMenu = (accountMenu) => {
  const accountMenuOn = accountMenu.classList.contains("d-block");
  if (accountMenuOn) {
    hideAccountMenu(accountMenu);
  } else {
    showAccountMenu(accountMenu);
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

/**
 * This will hide the sidebar when the cross at the top is clicked.
 */
const sideBarCross = document.querySelector("#openSidebarCross");
sideBarCross.addEventListener("click", () => {
  const sideBarMenu = document.querySelector("#sideBar");
  hideSideBar(sideBarMenu);
});

/**
 * This will hide or show the My Account menu bar when the account icon is clicked.
 */
const accountMenuIcon = document.querySelector("#myAccountSelector");
accountMenuIcon.addEventListener("click", () => {
  const accountSelector = document.querySelector("#accountMenu");
  myAccountMenu(accountSelector);
});
