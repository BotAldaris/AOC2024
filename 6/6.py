from enum import IntEnum
from collections import namedtuple
from time import time
from typing import Optional

Vec2 = namedtuple("Vec2", ["x", "y"])


class Direction(IntEnum):
    UP = 1
    LEFT = 2
    RIGHT = 3
    DOWN = 4


def extract_walls_and_player_from_text(
    lines: list[str],
) -> tuple[dict[int, list[int]], dict[int, list[int]], Vec2]:
    player = Vec2(0, 0)
    x: dict[int, list[int]] = dict()
    y: dict[int, list[int]] = dict()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            match lines[i][j]:
                case "#":
                    x_list = x.get(i, [])
                    x_list.append(j)
                    x[i] = x_list
                    y_list = y.get(j, [])
                    y_list.append(i)
                    y[j] = y_list
                case "^":
                    player = Vec2(i, j)
    return (x, y, player)


def is_wall_in_the_way(
    player: Vec2, x: dict[int, list[int]], y: dict[int, list[int]], direction: Direction
) -> tuple[bool, Vec2, Direction]:
    match direction:
        case Direction.UP:
            walls = reversed(y.get(player.y, []))
            for wall in walls:
                if player.x > wall:
                    return True, Vec2(wall + 1, player.y), Direction.RIGHT
        case Direction.RIGHT:
            walls_s = sorted(x.get(player.x, []))
            for wall in walls_s:
                if wall > player.y:
                    return True, Vec2(player.x, wall - 1), Direction.DOWN
        case Direction.DOWN:
            walls_s = sorted(y.get(player.y, []))
            for wall in walls_s:
                if wall > player.x:
                    return True, Vec2(wall - 1, player.y), Direction.LEFT
        case Direction.LEFT:
            walls = reversed(x.get(player.x, []))
            for wall in walls:
                if wall < player.y:
                    return True, Vec2(player.x, wall + 1), Direction.UP
    return False, Vec2(0, 0), direction


def vec2_to_str(x: int, y: int) -> str:
    return f"{x}|{y}"


def get_positions_between_old_and_new_position(
    old_position: Vec2, new_position: Vec2, direction: Direction, positions: set[str]
):
    match direction:
        case Direction.UP:
            for i in range(old_position.x - new_position.x + 1):
                positions.add(vec2_to_str(old_position.x - i, old_position.y))
        case Direction.DOWN:
            for i in range(new_position.x - old_position.x + 1):
                positions.add(vec2_to_str(new_position.x - i, old_position.y))
        case Direction.LEFT:
            for i in range(old_position.y - new_position.y + 1):
                positions.add(vec2_to_str(old_position.x, old_position.y - i))
        case Direction.RIGHT:
            for i in range(new_position.y - old_position.y + 1):
                positions.add(vec2_to_str(old_position.x, new_position.y - i))


def replace_char_at_index(s, index, new_char):
    if index < 0 or index >= len(s):
        raise ValueError("Índice fora do intervalo da string.")
    # Cria uma nova string com o caractere substituído
    return s[:index] + new_char + s[index + 1 :]


def end(player: Vec2, direction: Direction, lines: list[str], positions: set[str]):
    match direction:
        case Direction.UP:
            get_positions_between_old_and_new_position(
                player, Vec2(0, player.y), direction, positions
            )
        case Direction.DOWN:
            get_positions_between_old_and_new_position(
                player, Vec2(len(lines) - 1, player.y), direction, positions
            )
        case Direction.LEFT:
            get_positions_between_old_and_new_position(
                player, Vec2(player.x, 0), direction, positions
            )
        case Direction.RIGHT:
            get_positions_between_old_and_new_position(
                player, Vec2(player.x, len(lines[0]) - 2), direction, positions
            )


def parte1():
    begin = time()

    with open(r"6\6.txt", "r") as file:
        lines = file.readlines()
    x, y, player = extract_walls_and_player_from_text(lines)
    direction = Direction.UP
    has_wall = True
    positions = set()
    while 1:
        has_wall, new_player_position, new_direction = is_wall_in_the_way(
            player, x, y, direction
        )
        if has_wall:
            get_positions_between_old_and_new_position(
                player, new_player_position, direction, positions
            )
            direction = new_direction
            player = new_player_position
        else:
            break
        if (time() - begin) > 0.01:
            return 1
    end(player, direction, lines, positions)

    return 0


def win(lines: list[str]):
    begin = time()
    x, y, player = extract_walls_and_player_from_text(lines)
    direction = Direction.UP
    has_wall = True
    while 1:
        has_wall, new_player_position, new_direction = is_wall_in_the_way(
            player, x, y, direction
        )
        if has_wall:
            direction = new_direction
            player = new_player_position
        else:
            break
        if (time() - begin) > 0.01:
            return 1
    return 0


def parte2():
    begin = time()
    with open(r"6\6.txt", "r") as file:
        lines = file.readlines()
    x, y, player = extract_walls_and_player_from_text(lines)
    player_inicial = Vec2(player.x, player.y)
    direction = Direction.UP
    has_wall = True
    positions = set()
    while 1:
        has_wall, new_player_position, new_direction = is_wall_in_the_way(
            player, x, y, direction
        )
        if has_wall:
            get_positions_between_old_and_new_position(
                player, new_player_position, direction, positions
            )
            direction = new_direction
            player = new_player_position
        else:
            break
    end(player, direction, lines, positions)

    count = 0
    if vec2_to_str(player_inicial.x, player_inicial.y) in positions:
        positions.remove(vec2_to_str(player_inicial.x, player_inicial.y))
    for position in positions:
        xy = list(map(int, position.split("|")))
        x2 = x.copy()
        x_list = x2.get(xy[0], [])
        x_list.append(xy[1])
        x2[xy[0]] = x_list
        y2 = y.copy()
        y_list = y2.get(xy[1], [])
        y_list.append(xy[0])
        y2[xy[1]] = y_list
        pp = set()
        pp.add(position)
        lines_2 = lines.copy()
        lines_2[xy[0]] = replace_char_at_index(lines_2[xy[0]], xy[1], "#")
        if win(lines_2):
            count += 1
    print(count)
    print((time() - begin))


parte2()
