#!/bin/bash

MARKERS=("o" "x")
SAVE_PATH="./game_save"
MOVE_REGEX='^[0-2]$'
MENU_REGEX='^[1-3]$'

function reset_game {
    BOARD_STATUS=(" " " " " " " " " " " " " " " " " ")
    game_status=0
    move_result=0
    current_player=0
    total_moves=0
}

function get_field {
    echo "Player $current_player"
    while [ "$move_result" != "1" ]; do
        echo "Insert row"
        read row
        echo "Insert column"
        read column
        validate_move $row $column
        move_result=$?
    done

    BOARD_STATUS[$(((3 * $row) + $column))]=${MARKERS[current_player]}
}

function switch_players {
    if [ "$game_status" != "1" ]; then
        current_player=$((($current_player + 1) % 2))
    fi
}

function check_status {
    echo
    for i in {0..2}; do
        if [ "${BOARD_STATUS[$(((3 * i) + 0))]}" == "${MARKERS[current_player]}" ] &&
            [ "${BOARD_STATUS[$(((3 * i) + 1))]}" == "${MARKERS[current_player]}" ] &&
            [ "${BOARD_STATUS[$(((3 * i) + 2))]}" == "${MARKERS[current_player]}" ]; then
            return 1
        fi

        if [ "${BOARD_STATUS[$((i))]}" == "${MARKERS[current_player]}" ] &&
            [ "${BOARD_STATUS[$((3 + i))]}" == "${MARKERS[current_player]}" ] &&
            [ "${BOARD_STATUS[$((6 + i))]}" == "${MARKERS[current_player]}" ]; then
            return 1
        fi

        if [ "${BOARD_STATUS[0]}" == "${MARKERS[current_player]}" ] &&
            [ "${BOARD_STATUS[4]}" == "${MARKERS[current_player]}" ] &&
            [ "${BOARD_STATUS[8]}" == "${MARKERS[current_player]}" ]; then
            return 1
        fi

        if [ "${BOARD_STATUS[2]}" == "${MARKERS[current_player]}" ] &&
            [ "${BOARD_STATUS[4]}" == "${MARKERS[current_player]}" ] &&
            [ "${BOARD_STATUS[6]}" == "${MARKERS[current_player]}" ]; then
            return 1
        fi
    done
}

function print_game_status {
    if [ "$game_status" == "1" ]; then
        echo "Player $current_player wins!! "
    else
        echo "Draw!! "
    fi
    clear_save
}

function print_board {
    echo "  -----------------"
    echo "0 | ${BOARD_STATUS[0]}  |  ${BOARD_STATUS[1]}  |  ${BOARD_STATUS[2]} |"
    echo "  |---------------|"
    echo "1 | ${BOARD_STATUS[3]}  |  ${BOARD_STATUS[4]}  |  ${BOARD_STATUS[5]} |"
    echo "  |---------------|"
    echo "2 | ${BOARD_STATUS[6]}  |  ${BOARD_STATUS[7]}  |  ${BOARD_STATUS[8]} |"
    echo "  -----------------"
    echo "    0     1    2"

}

function validate_move() {

    if [[ ! $1 =~ $MOVE_REGEX ]] || [[ ! $2 =~ $MOVE_REGEX ]]; then
        echo "Entered wrong column or line, please enter correct one "
        return 0
    elif [ "${BOARD_STATUS[$(((3 * $1) + $2))]}" != " " ]; then
        echo "This field is taken, select another one"
        return 0
    else
        return 1
    fi

}

function update_state {
    total_moves=$(($total_moves + 1))
    move_result=0
}

function start_new_game {
    reset_game
    clear_save
    start_game
}

function load_save {
    if [ -e $SAVE_PATH ]; then

        reset_game
        readarray -t BOARD_STATUS <${SAVE_PATH}
        local move_counter=0
        for i in {0..8}; do
            if [[ "${BOARD_STATUS[$i]}" != " " ]]; then
                move_counter=$(($move_counter + 1))
            fi
        done
        echo "$move_counter"
        current_player=$(($move_counter % 2))
        start_game
    else
        echo "Save file does not exist "
    fi
}

function make_save {
    if [ -e ${SAVE_PATH} ]; then
        touch $SAVE_PATH
    fi
    : >${SAVE_PATH}

    for i in {1..9}; do
        echo "${BOARD_STATUS[$i - 1]}" >>$SAVE_PATH
    done
}

function clear_save {
    if [ -e $SAVE_PATH ]; then
        rm -f $SAVE_PATH
    fi
}

function start_game {
    while [ "$game_status" != "1" ] && [ $total_moves != 9 ]; do
        clear
        print_board
        get_field
        check_status
        game_status=$?
        update_state
        switch_players
        make_save
    done
    print_game_status
}

function show_menu {
    local choice=0

    echo "1. New Game"
    echo "2. Load save"
    echo "3. Exit"

    while [[ ! $choice =~ $MENU_REGEX ]]; do
        read choice
        if [ "$choice" == "1" ]; then
            clear
            start_new_game
        elif [ "$choice" == "2" ]; then
            clear
            load_save
        elif [ "$choice" == "3" ]; then
            echo "Exiting"
            clear
        fi
    done

}

show_menu
