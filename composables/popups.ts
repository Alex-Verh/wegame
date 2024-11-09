export const usePopup = (popup: string) => {
  const popupVisibility = useState(popup, () => false);

  return {
    visible: popupVisibility,
    open: () => {
      popupVisibility.value = true;
    },
    close: () => {
      popupVisibility.value = false;
    },
  };
};
export const useProfilePopup = () => usePopup("profilePopup");
export const useUserDetailsPopup = () => usePopup("userDetailsPopup");
export const useUserLinksPopup = () => usePopup("userLinksPopup");
export const useNewApplicationPopup = () => usePopup("newApplicationPopup");
export const useNewPartyPopup = () => usePopup("newPartyPopup");
export const usePartyMembersPopup = () => usePopup("partyMembersPopup");
