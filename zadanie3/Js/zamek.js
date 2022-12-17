function ZbudujWieze(position: Position) {
  blocks.fill(
    COBBLESTONE,
    position,
    positions.add(
      position,
      pos(4, 12, 4)
    ),
    FillOperation.Replace
  )
  blocks.place(LOG_SPRUCE, positions.add(
    position,
    pos(0, 13, 0)
  ))
  blocks.place(LOG_SPRUCE, positions.add(
    position,
    pos(0, 13, 2)
  ))
  blocks.place(LOG_SPRUCE, positions.add(
    position,
    pos(0, 13, 4)
  ))
  blocks.place(LOG_SPRUCE, positions.add(
    position,
    pos(2, 13, 4)
  ))
  blocks.place(LOG_SPRUCE, positions.add(
    position,
    pos(4, 13, 4)
  ))
  blocks.place(LOG_SPRUCE, positions.add(
    position,
    pos(4, 13, 2)
  ))
  blocks.place(LOG_SPRUCE, positions.add(
    position,
    pos(4, 13, 0)
  ))
  blocks.place(LOG_SPRUCE, positions.add(
    position,
    pos(2, 13, 0)
  ))
  blocks.place(REDSTONE_TORCH, positions.add(
    position,
    pos(0, 14, 0)
  ))
  blocks.place(REDSTONE_TORCH, positions.add(
    position,
    pos(4, 14, 0)
  ))
  blocks.place(REDSTONE_TORCH, positions.add(
    position,
    pos(4, 14, 4)
  ))

  blocks.place(REDSTONE_TORCH, positions.add(
    position,
    pos(0, 14, 4)
  ))
}

blocks.fill(
  STONE,
  pos(1, 0, 1),
  pos(30, 8, 1),
  FillOperation.Replace
)

blocks.fill(
  STONE,
  pos(30, 0, 1),
  pos(30, 8, 30),
  FillOperation.Replace
)

blocks.fill(
  STONE,
  pos(30, 0, 30),
  pos(1, 8, 30),
  FillOperation.Replace
)

blocks.fill(
  STONE,
  pos(1, 0, 30),
  pos(1, 8, 1),
  FillOperation.Replace
)

blocks.place(OAK_WOOD_STAIRS, pos(0, 0, 15))
blocks.place(OAK_WOOD_STAIRS, pos(0, 0, 16))

blocks.place(CRIMSON_DOOR, pos(1, 1, 15))
blocks.place(CRIMSON_DOOR, pos(1, 1, 16))

ZbudujWieze(pos(1, 0, 1))
ZbudujWieze(pos(26, 0, 1))
ZbudujWieze(pos(26, 0, 26))
ZbudujWieze(pos(1, 0, 26))

blocks.fill(
  GLASS,
  pos(10, 3, 1),
  pos(20, 5, 1),
  FillOperation.Replace
)

blocks.fill(
  GLASS,
  pos(10, 3, 30),
  pos(20, 5, 30),
  FillOperation.Replace
)

blocks.fill(
  GLASS,
  pos(1, 3, 10),
  pos(1, 5, 20),
  FillOperation.Replace
)

blocks.fill(
  GLASS,
  pos(30, 3, 10),
  pos(30, 5, 20),
  FillOperation.Replace
)

blocks.fill(
  MOSSY_STONE_BRICKS,
  pos(1, 0, 1),
  pos(30, 0, 30),
  FillOperation.Replace
)

blocks.fill(
  WATER,
  pos(-10, -1, -10),
  pos(-7, -3, 40),
  FillOperation.Replace
)

blocks.fill(
  WATER,
  pos(-10, -1, 40),
  pos(40, -3, 36),
  FillOperation.Replace
)

blocks.fill(
  WATER,
  pos(40, -1, 40),
  pos(36, -3, -10),
  FillOperation.Replace
)

blocks.fill(
  WATER,
  pos(40, -1, -10),
  pos(-10, -3, -7),
  FillOperation.Replace
)
blocks.fill(
  GRANITE,
  pos(0, -1, 14),
  pos(-6, -1, 17),
  FillOperation.Replace
)

blocks.fill(
  PLANKS_DARK_OAK,
  pos(-7, -1, 14),
  pos(-10, -1, 17),
  FillOperation.Replace
)

blocks.fill(
  DARK_OAK_FENCE,
  pos(-7, 0, 14),
  pos(-10, 0, 14),
  FillOperation.Replace
)

blocks.fill(
  DARK_OAK_FENCE,
  pos(-7, 0, 17),
  pos(-10, 0, 17),
  FillOperation.Replace
)

blocks.fill(
  GRANITE,
  pos(-11, -1, 14),
  pos(-15, -1, 17),
  FillOperation.Replace
)