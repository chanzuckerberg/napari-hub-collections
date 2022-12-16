import sharp from 'sharp'
import fs from 'fs'
import path from 'path'
import prettyBytes from 'pretty-bytes'

const SUPPORTED_IMAGE_EXTENSIONS = ['jpeg', 'jpg', 'png']

const imageFiles = fs
  .readdirSync('.')
  .filter(
    file =>
      !file.includes('-thumb') &&
      SUPPORTED_IMAGE_EXTENSIONS.some(ext => file.includes(ext))
  )

function getThumbFile(file) {
  const ext = path.extname(file)
  const name = path.basename(file, ext)
  return `${name}-thumb${ext}`
}

/**
 * The max observed width for images in the browser. This happens between 600px
 * and 875px when the page is using a 2 column flexible layout.
 */
const THUMB_IMAGE_WIDTH = 500

function convertImages() {
  console.log(`Resizing ${imageFiles.length} images`)

  imageFiles.forEach(async file => {
    const image = sharp(file)
    const metadata = await image.metadata()

    if ((metadata.width ?? 0) > THUMB_IMAGE_WIDTH) {
      image.resize(THUMB_IMAGE_WIDTH).toFile(getThumbFile(file), err => {
        if (err) {
          console.error(`Unable to resize image`, err)
        }
      })
    }
  })
}

async function compareImages() {
  for (const file of imageFiles) {
    const thumbFile = getThumbFile(file)
    const image = sharp(file)
    const thumbImage = sharp(thumbFile)
    const metadata = await image.metadata()
    const thumbMetadata = await thumbImage.metadata()

    const stats = fs.statSync(file)
    const thumbStats = fs.statSync(thumbFile)

    console.log(file)
    console.log(`  Dimensions       => ${metadata.width} x ${metadata.height}`)
    console.log(
      `  Thumb Dimensions => ${thumbMetadata.width} x ${thumbMetadata.height}`
    )
    console.log(`  Size             => ${prettyBytes(stats.size)}`)
    console.log(`  Thumb Size       => ${prettyBytes(thumbStats.size)}`)
    console.log()
  }
}

function main([action]) {
  switch (action) {
    case 'compare':
      compareImages()
      break

    default:
      convertImages()
      break
  }
}

main(process.argv.slice(2))
