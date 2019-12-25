# 所有轨道全部还原为默认的状态
def reset():
    if RPR_CountTracks(0) == 0:
        return

    RPR_Undo_BeginBlock()
    track_num = RPR_CountTracks(0)

    for i in range(track_num):
        temp_track = RPR_GetTrack(0, i)
        RPR_SetOnlyTrackSelected(temp_track)
        cur_track_item_num = RPR_CountTrackMediaItems(temp_track)
        RPR_Main_OnCommand(40421, 0)
        items_l = []

        for j in range(cur_track_item_num):
            item = RPR_GetSelectedMediaItem(0, j)
            items_l.append(item)

        RPR_InsertTrackAtIndex(i, True)
        add_track = RPR_GetTrack(0, i)

        for i in items_l:
            RPR_MoveMediaItemToTrack(i, add_track)

        RPR_DeleteTrack(temp_track)

    RPR_Undo_EndBlock("reset", -1)

reset()
