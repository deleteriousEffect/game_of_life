# Load board from presets file

# Display board

# Update board
    # Check every cell
        # If live
            # Any Cell with fewer than two neighbors dies
            # Any Cell with two or three neighbors lives on
            # Any Cell with more than three neighbors dies
        # If dead
            # Any dead Cell with exactly three neighbors becomes a live Cell
    # Loop every 300? miliseconds until stable pattern or interrupt
