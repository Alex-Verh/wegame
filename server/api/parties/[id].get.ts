export default defineEventHandler(async (event) => {
    const { id } = await getValidatedRouterParams(
      event,
      z.object({ id: z.coerce.number() }).parse
    );
  
    const db = useDrizzle();
  
    const party = await db.query.applications.findFirst({
      where: eq(tables.parties.id, id),
    });
    return party;
  });
  