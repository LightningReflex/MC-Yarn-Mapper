# MC-Yarn-Mapper
Super cool mapping tool to do stuff like this:
```
[13:45:53] [Render thread/WARN]: Ignoring chunk since it's not in the view range: -17, 6
[13:45:53] [Render thread/WARN]: Ignoring chunk since it's not in the view range: 3, -14
[13:45:56] [Render thread/ERROR]: Failed to handle packet net.minecraft.class_2629@4c542a03, disconnecting
java.lang.NullPointerException: Cannot invoke "net.minecraft.class_345.method_5408(float)" because the return value of "java.util.Map.get(Object)" is null
    at knot/net.minecraft.class_337$1.method_34100(class_337.java:124) ~[client-intermediary.jar:?]
    at knot/net.minecraft.class_2629$class_5885.method_34106(class_2629.java:216) ~[client-intermediary.jar:?]
    at knot/net.minecraft.class_2629.method_34091(class_2629.java:91) ~[client-intermediary.jar:?]
    at knot/net.minecraft.class_337.method_1795(class_337.java:111) ~[client-intermediary.jar:?]
    at knot/net.minecraft.class_634.method_11078(class_634.java:1952) ~[client-intermediary.jar:?]
    at knot/net.minecraft.class_2629.method_11330(class_2629.java:87) ~[client-intermediary.jar:?]
    at knot/net.minecraft.class_2629.method_65081(class_2629.java:14) ~[client-intermediary.jar:?]
    at knot/net.minecraft.class_2600.method_11072(class_2600.java:27) ~[client-intermediary.jar:?]
    at knot/net.minecraft.class_1255.method_18859(class_1255.java:164) [client-intermediary.jar:?]
    at knot/net.minecraft.class_4093.method_18859(class_4093.java:23) [client-intermediary.jar:?]
    at knot/net.minecraft.class_1255.method_16075(class_1255.java:138) [client-intermediary.jar:?]
    at knot/net.minecraft.class_1255.method_5383(class_1255.java:123) [client-intermediary.jar:?]
    at knot/net.minecraft.class_310.method_1523(class_310.java:1296) [client-intermediary.jar:?]
    at knot/net.minecraft.class_310.method_1514(class_310.java:922) [client-intermediary.jar:?]
    at knot/net.minecraft.client.main.Main.main(Main.java:267) [client-intermediary.jar:?]
    at net.fabricmc.loader.impl.game.minecraft.MinecraftGameProvider.launch(MinecraftGameProvider.java:480) [fabric-loader-0.16.14.jar:?]
    at net.fabricmc.loader.impl.launch.knot.Knot.launch(Knot.java:74) [fabric-loader-0.16.14.jar:?]
    at net.fabricmc.loader.impl.launch.knot.KnotClient.main(KnotClient.java:23) [fabric-loader-0.16.14.jar:?]
    at org.prismlauncher.launcher.impl.StandardLauncher.launch(StandardLauncher.java:100) [NewLaunch.jar:?]
    at org.prismlauncher.EntryPoint.listen(EntryPoint.java:129) [NewLaunch.jar:?]
    at org.prismlauncher.EntryPoint.main(EntryPoint.java:70) [NewLaunch.jar:?]
[13:45:57] [Render thread/INFO]: Stopping worker threads
[13:45:57] [Render thread/WARN]: Client disconnected with reason: Network Protocol Error
```

Into something more readable such as this:
```[13:45:53] [Render thread/WARN]: Ignoring chunk since it's not in the view range: -17, 6
[13:45:53] [Render thread/WARN]: Ignoring chunk since it's not in the view range: 3, -14
[13:45:56] [Render thread/ERROR]: Failed to handle packet net.minecraft.BossBarS2CPacket@4c542a03, disconnecting
java.lang.NullPointerException: Cannot invoke "net.minecraft.ClientBossBar.setPercent(float)" because the return value of "java.util.Map.get(Object)" is null
    at knot/net.minecraft.BossBarHud$1.updateProgress(BossBarHud.java:124) ~[client-intermediary.jar:?]
    at knot/net.minecraft.BossBarS2CPacket$UpdateProgressAction.accept(BossBarS2CPacket.java:216) ~[client-intermediary.jar:?]
    at knot/net.minecraft.BossBarS2CPacket.accept(BossBarS2CPacket.java:91) ~[client-intermediary.jar:?]
    at knot/net.minecraft.BossBarHud.handlePacket(BossBarHud.java:111) ~[client-intermediary.jar:?]
    at knot/net.minecraft.ClientPlayNetworkHandler.onBossBar(ClientPlayNetworkHandler.java:1952) ~[client-intermediary.jar:?]
    at knot/net.minecraft.BossBarS2CPacket.apply(BossBarS2CPacket.java:87) ~[client-intermediary.jar:?]
    at knot/net.minecraft.BossBarS2CPacket.method_65081(BossBarS2CPacket.java:14) ~[client-intermediary.jar:?]
    at knot/net.minecraft.NetworkThreadUtils.method_11072(NetworkThreadUtils.java:27) ~[client-intermediary.jar:?]
    at knot/net.minecraft.ThreadExecutor.executeTask(ThreadExecutor.java:164) [client-intermediary.jar:?]
    at knot/net.minecraft.ReentrantThreadExecutor.executeTask(ReentrantThreadExecutor.java:23) [client-intermediary.jar:?]
    at knot/net.minecraft.ThreadExecutor.runTask(ThreadExecutor.java:138) [client-intermediary.jar:?]
    at knot/net.minecraft.ThreadExecutor.runTasks(ThreadExecutor.java:123) [client-intermediary.jar:?]
    at knot/net.minecraft.MinecraftClient.render(MinecraftClient.java:1296) [client-intermediary.jar:?]
    at knot/net.minecraft.MinecraftClient.run(MinecraftClient.java:922) [client-intermediary.jar:?]
    at knot/net.minecraft.client.main.Main.main(Main.java:267) [client-intermediary.jar:?]
    at net.fabricmc.loader.impl.game.minecraft.MinecraftGameProvider.launch(MinecraftGameProvider.java:480) [fabric-loader-0.16.14.jar:?]
    at net.fabricmc.loader.impl.launch.knot.Knot.launch(Knot.java:74) [fabric-loader-0.16.14.jar:?]
    at net.fabricmc.loader.impl.launch.knot.KnotClient.main(KnotClient.java:23) [fabric-loader-0.16.14.jar:?]
    at org.prismlauncher.launcher.impl.StandardLauncher.launch(StandardLauncher.java:100) [NewLaunch.jar:?]
    at org.prismlauncher.EntryPoint.listen(EntryPoint.java:129) [NewLaunch.jar:?]
    at org.prismlauncher.EntryPoint.main(EntryPoint.java:70) [NewLaunch.jar:?]
[13:45:57] [Render thread/INFO]: Stopping worker threads
[13:45:57] [Render thread/WARN]: Client disconnected with reason: Network Protocol Error
```