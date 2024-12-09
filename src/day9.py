from collections import namedtuple

Block = namedtuple("Block", ["start_index", "length"])


def part_1(raw_input: list[str]) -> int:
    file_blocks, free_space = parse_input(raw_input)
    compacted_blocks = block_compaction(file_blocks, free_space)
    return disk_hash(compacted_blocks)


def part_2(raw_input: list[str]) -> int:
    file_blocks, free_space = parse_input(raw_input)
    compacted_blocks = file_compaction(file_blocks, free_space)
    return disk_hash(compacted_blocks)


def parse_input(raw_input):
    disk_map: str = raw_input[0]
    file_blocks: list[list[Block]] = []
    free_space: list[Block] = []
    starting_block: int = 0
    for loc in range(len(disk_map)):
        is_free_space: bool = loc % 2 == 1
        length: int = int(disk_map[loc])
        block: Block = Block(starting_block, length)
        if length == 0:
            continue
        elif is_free_space:
            free_space.append(block)
        else:
            file_blocks.append([block])
        starting_block += length
    return file_blocks, free_space


def block_compaction(file_bounds: list[list[Block]], free_space: list[Block]) -> list[list[Block]]:
    for file in reversed(file_bounds):
        while file[0].length > 0:
            block: Block = file[0]
            location_to_compact_from: int = block.start_index + block.length - 1
            length_to_compact: int = 1
            free_block, earliest_free_space = find_earliest_free_space_with_length(free_space, length_to_compact)
            if earliest_free_space > location_to_compact_from or earliest_free_space < 0:
                break  # Can't compact
            free_space = consume_free_space(free_space, free_block, length_to_compact)
            # Move file to new location
            if file[-1].start_index + file[-1].length == earliest_free_space:
                # Can extend most recent new block
                file[-1] = Block(file[-1].start_index, file[-1].length + length_to_compact)
            else:
                # Need new block
                file.append(Block(earliest_free_space, length_to_compact))
            file[0] = Block(block.start_index, block.length - length_to_compact)

    return file_bounds


def file_compaction(file_bounds: list[list[Block]], free_space: list[Block]) -> list[list[Block]]:
    for file in reversed(file_bounds):
        block: Block = file[0]
        location_to_compact_from: int = block.start_index + block.length - 1
        length_to_compact: int = block.length
        free_block, earliest_free_space = find_earliest_free_space_with_length(free_space, length_to_compact)
        if earliest_free_space > location_to_compact_from or earliest_free_space < 0:
            continue  # Can't compact
        free_space = consume_free_space(free_space, free_block, length_to_compact)
        # Move file to new location
        file[0] = Block(earliest_free_space, block.length)
    return file_bounds


def consume_free_space(free_space: list[Block], free_block: int, length_to_compact: int) -> list[Block]:
    free_space[free_block] = Block(free_space[free_block].start_index + length_to_compact,
                                   free_space[free_block].length - length_to_compact)
    if free_space[free_block].length == 0:
        free_space.pop(free_block)
    return free_space


def find_earliest_free_space(free_space: list[Block]) -> int:
    return -1 if len(free_space) == 0 else free_space[0].start_index


def find_earliest_free_space_with_length(free_space: list[Block], length: int) -> (int, int):
    for block_id, free_space_block in enumerate(free_space):
        if free_space_block.length >= length:
            return block_id, free_space_block.start_index
    return -1, -1


def disk_hash(compacted_blocks: list[list[Block]]) -> int:
    hash_value: int = 0
    for block_id in range(len(compacted_blocks)):
        file = compacted_blocks[block_id]
        for block in file:
            for index in range(block.length):
                hash_value += (block.start_index + index) * block_id
    return hash_value
