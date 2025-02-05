export interface Toast {
  id: number;
  content: string;
  variant: string;
}

export const useToast = (content: string, variant: string = "primary") => {
  const toasts = useState<Toast[]>("toasts", () => []);
  const id = Date.now();
  toasts.value.push({ id, content, variant });

  setTimeout(() => {
    toasts.value = toasts.value.filter((toast) => toast.id !== id);
  }, 5000);
};
