export const invalidCredentialsError = createError({
  statusCode: 401,
  message: "Invalid credentials",
});

export const userNotFoundError = createError({
  statusCode: 404,
  message: "User not found",
});

export const userAlreadyExistsError = createError({
  statusCode: 409,
  message: "User already exists",
});

export const userNotActiveError = createError({
  statusCode: 403,
  message: "User is not active",
});

export const forbiddenError = createError({
  statusCode: 403,
  message: "Forbidden",
});

export const deletionError = createError({
  statusCode: 400,
  message: "Counld not delete",
});

export const validationError = createError({
  statusCode: 400,
  message: "Validation error",
});
