import { CapacitorUpdater } from '@capgo/capacitor-updater';

import { Dialog } from '@capacitor/dialog'

CapacitorUpdater.addListener('updateAvailable', async (res) => {
  try {
    const { value } = await Dialog.confirm({
      title: 'Update Available',
      message: `Version ${res.bundle.version} is available. Would you like to update now?`,
    })

    if (value)
      CapacitorUpdater.set(res.bundle)

  }
  catch (error) {
    console.log(error)
  }
})

CapacitorUpdater.notifyAppReady();
console.log('CapacitorUpdater Loaded');
