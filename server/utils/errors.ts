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
