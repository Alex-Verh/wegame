export default defineEventHandler(async (event) => {
  const { id } = await getValidatedRouterParams(
    event,
    z.object({ id: z.coerce.number() }).parse
  );

  const db = useDrizzle();

  const application = await db.query.applications.findFirst({
    where: eq(tables.applications.id, id),
  });
  return application;
});
