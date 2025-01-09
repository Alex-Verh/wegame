export const usePopup = () => {
  const popupVisibility = ref(false);
  return {
    isOpen: popupVisibility,
    open: () => {
      popupVisibility.value = true;
    },
    close: () => {
      popupVisibility.value = false;
    },
  };2
};
