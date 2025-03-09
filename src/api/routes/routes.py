


from sqlalchemy import outerjoin


@outerjoin.post("/post", response_model=ChildInDB, name="Children: create-child", status_code=status.HTTP_201_CREATED)
async def post_child(
    child_new: ChildCreate,
    child_repo: ChildRepository = Depends(get_repository(ChildRepository)),
) -> ChildInDB:
    child_created = await child_repo.create(obj_new=child_new)

    return child_created

@router.get("/get_by_id", response_model=ChildInDB | None, name="children: read-one-child")
async def get_one_child(
    id: int,
    child_repo: ChildRepository = Depends(get_repository(ChildRepository)),
) -> ChildInDB | None:
     child_db = await child_repo.read_by_id(id=id)
     if not child_db:
        logger.warning(f"No child with id = {id}.")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No child with id = {id}.")

     return child_db