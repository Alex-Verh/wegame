import { useVfm } from "vue-final-modal";

export const usePopup = (id: string) => {
  const vfm = useVfm();
  const modalId = Symbol(id);

  const open = () => {
    vfm.open(modalId);
  };
  const close = () => {
    vfm.close(modalId);
  };

  return { modalId, open, close };
};

export { useModal } from "vue-final-modal";
