#playerbackpack = Player.Backpack.Serial
#Items.Move(0x41C8D559, playerbackpack, 10)

Items.UseItemByID(0x0E73, -1)
Target.WaitForTarget(10000, False)
Target.TargetExecute(0x441D3E16)
Misc.Pause(1000)
Items.UseItemByID(0x0E73, -1)
Target.WaitForTarget(10000, False)
Target.TargetExecute(0x441D3E1E)

#Items.UseItem(0x41C8D559)
#Target.WaitForTarget(10000, False)
#Target.TargetExecute(0x441D3E16)
#Items.Move(0x441DC3B9, 0x40198FF0, 0)
#Items.UseItem(0x441DC3B9)
#Target.WaitForTarget(10000, False)
#Target.TargetExecute(0x441D3E1E)
#Player.ChatSay(52, "fire right")
#Target.WaitForTarget(10000, False)
#Target.TargetExecute(4552, 766 ,-2 ,16033)
#Player.ChatSay(52, "fire left")
#Target.WaitForTarget(10000, False)
#Target.TargetExecute(4541, 769 ,-2 ,16033)