import { CapacitorUpdater } from "@capgo/capacitor-updater";

import { Dialog } from "@capacitor/dialog";
console.log("NARF");
CapacitorUpdater.addListener("updateAvailable", async (res) => {
  console.log("PRE RES", res);
  try {
    const { value } = await Dialog.confirm({
      title: "Update Available",
      message: `Version ${res.bundle.version} is available. Would you like to update now?`,
    });

    console.log("RES", res);
    if (value) {
      CapacitorUpdater.set(res.bundle);
    }
  } catch (error) {
    console.log("UPDATER ERROR", error);
  }
});

CapacitorUpdater.notifyAppReady();
console.log("CapacitorUpdater Loaded");
