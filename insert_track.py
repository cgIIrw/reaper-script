def insert_track():
    # 该函数计算当前工程选择的items数目
    if RPR_CountSelectedMediaItems(0)==0:
        return

    # 还原点
    RPR_Undo_BeginBlock()
    # 获取第一轨
    first_track = RPR_GetTrack(0, 0)
    # 获取第一轨的轨道名
    first_track_name = RPR_GetSetMediaTrackInfo_String(first_track, 'P_NAME', '', False)[3]

    if first_track_name == 'Audition':
        # 单选第一轨
        RPR_SetOnlyTrackSelected(first_track)
        # 移除选中的轨道
        RPR_Main_OnCommand(40005, 0)

    # 在首位插入轨道
    RPR_InsertTrackAtIndex(0, True)
    first_track = RPR_GetTrack(0, 0)
    # 为轨道设置轨道名
    RPR_GetSetMediaTrackInfo_String(first_track, 'P_NAME', 'Audition', True)
    # 创建列表
    items_l = []
    # 获取选中的item的数目
    itemsNum = RPR_CountSelectedMediaItems(0)

    # 将所有选中的items插入创建的列表中
    for i in range(itemsNum):
        item = RPR_GetSelectedMediaItem(0, i)
        items_l.append(item)

    for i in items_l:
        # 全部unselect
        RPR_Main_OnCommand(40289, 0)
        # 选中指定的item
        RPR_SetMediaItemSelected(i, True)
        # Apply track/take FX to items
        RPR_Main_OnCommand(40209, 0)
        # Move active comp to top lane
        RPR_Main_OnCommand(41378, 0)
        # explode takes of items in place
        RPR_Main_OnCommand(40642, 0)
        # 选中指定的item
        RPR_SetMediaItemSelected(i, True)
        # 将选中的item移动到指定track
        RPR_MoveMediaItemToTrack(i, first_track)

    # 单选第一轨
    RPR_SetOnlyTrackSelected(first_track)
    # select all items in track
    RPR_Main_OnCommand(40421, 0)
    # Glue items
    RPR_Main_OnCommand(41588, 0)
    RPR_Undo_EndBlock("insert_track", -1)

insert_track()
