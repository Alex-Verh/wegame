import { H3Event } from "h3";
export const requireAdminUserSession = async (event: H3Event) => {
  const session = await requireUserSession(event);
  if (!session.user.isSuperuser) {
    throw forbiddenError;
  }
  return session;
};
