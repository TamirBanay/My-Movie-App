import { atom } from "recoil";

export const _moviesList = atom({
  key: "_moviesList",
  default: [],
});
export const _currentPage = atom({
  key: "_currentPage",
  default: 1,
});
export const _movieIsOpen = atom({
  key: "_movieIsOpen",
  default: false,
});
export const _movieId = atom({
  key: "_movieId",
  default: null,
});
export const _userIsLoggedIn = atom({
  key: "_userIsLoggedIn",
  default: localStorage.getItem("isLoggedIn") || false,
});

export const _currentUserId = atom({
  key: "_currentUserId",
  default: null,
});
export const _user = atom({
  key: "_user",
  default: [],
});
export const _favoritMovies = atom({
  key: "_favoritMovies",
  default: [],
});
export const _favoritMoviesDetails = atom({
  key: "_favoritMoviesDetails",
  default: [],
});

export const _isLiked = atom({
  key: "_isLiked",
  default: false,
});
export const _isDark = atom({
  key: "_isDark",
  default: localStorage.getItem("theme") || "light",
});
export const _selectType = atom({
  key: "_selectType",
  default: "now_playing",
});
export const _recommendadMovies = atom({
  key: "_recommendadMovies",
  default: [],
});
