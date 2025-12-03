import { test, expect} from '@playwright/test'
import { describe } from 'node:test'



describe('RegexForm', () => {
  
  test('front page is opened with regexform', async ({ page }) => {
    await page.goto('http://localhost:5173')

    await expect(page.getByText('Säännöllisestä lausekkeesta DFA:ksi')).toBeVisible()
    await expect(page.getByText('Syötä säännöllinen lauseke:')).toBeVisible()
    await expect(page.getByRole('button', { name: 'Luo DFA' })).toBeVisible()
    await expect(page.getByTitle('Info')).toContainText('Sallitut operaatiot:')
  })

  test('dfa is created with valid input', async ({page}) => {
    await page.goto('http://localhost:5173')
    await page.getByRole('textbox').fill('a')
    await page.getByRole('button', { name: 'Luo DFA' }).click()
    await expect(page.getByText('Säännöllisen lausekkeen "a" DFA:')).toBeVisible()
    await expect(page.getByRole('button', { name: 'Näytä kuva' })).toBeVisible()
    await expect(page.getByRole('button', { name: 'Aloita alusta' })).toBeVisible()
    await expect(page.getByText('Syötä säännöllinen lauseke:')).not.toBeVisible()

  })
  test('dfa information is cleared and regexform showed after pressing button Aloita alusta', async ({page}) => {
    await page.goto('http://localhost:5173')
    await page.getByRole('textbox').fill('a')
    await page.getByRole('button', { name: 'Luo DFA' }).click()
    await page.getByRole('button', { name: 'Aloita alusta' }).click()
    await expect(page.getByText('Syötä säännöllinen lauseke:')).toBeVisible()
    await expect(page.getByRole('button', { name: 'Näytä kuva' })).not.toBeVisible()

  })

  test('error notification is rendered after empty input', async ({page}) => {
    await page.goto('http://localhost:5173')
    await page.getByRole('textbox').fill('')
    await page.getByRole('button', { name: 'Luo DFA' }).click()
    await expect(page.getByText('Virheellinen syöte: Syöte ei voi olla tyhjä.')).toBeVisible()
    await expect(page.getByText('Syötä säännöllinen lauseke:')).toBeVisible()
    await expect(page.getByRole('button', { name: 'Näytä kuva' })).not.toBeVisible()

  })

  test('error notification is rendered after invalid parenthesis use', async ({page}) => {
    await page.goto('http://localhost:5173')
    await page.getByRole('textbox').fill('((ab)')
    await page.getByRole('button', { name: 'Luo DFA' }).click()
    await expect(page.getByText('Virheellinen syöte: Tarkista sulkeiden käyttö.')).toBeVisible()
    await expect(page.getByText('Syötä säännöllinen lauseke:')).toBeVisible()
    await expect(page.getByRole('button', { name: 'Näytä kuva' })).not.toBeVisible()
    await page.getByRole('textbox').fill('a()*')
    await expect(page.getByText('Virheellinen syöte: Tarkista sulkeiden käyttö.')).toBeVisible()
    await expect(page.getByText('Syötä säännöllinen lauseke:')).toBeVisible()
    await expect(page.getByRole('button', { name: 'Näytä kuva' })).not.toBeVisible()

  })

  test('error notification is rendered after invalid symbols ', async ({page}) => {
    await page.goto('http://localhost:5173')
    await page.getByRole('textbox').fill('ha?')
    await page.getByRole('button', { name: 'Luo DFA' }).click()
    await expect(page.getByText('Syöte sisältää virheellisiä merkkejä.')).toBeVisible()
    await expect(page.getByText('Syötä säännöllinen lauseke:')).toBeVisible()
    await expect(page.getByRole('button', { name: 'Näytä kuva' })).not.toBeVisible()

  })

  test('error notification is rendered after input with whitespaces', async ({page}) => {
    await page.goto('http://localhost:5173')
    await page.getByRole('textbox').fill('a ')
    await page.getByRole('button', { name: 'Luo DFA' }).click()
    await expect(page.getByText('Virheellinen syöte: Poista välilyönnit.')).toBeVisible()
    await expect(page.getByText('Syötä säännöllinen lauseke:')).toBeVisible()
    await expect(page.getByRole('button', { name: 'Näytä kuva' })).not.toBeVisible()

  })

  test('error notification is rendered after input with invalid first symbol', async ({page}) => {
    await page.goto('http://localhost:5173')
    await page.getByRole('textbox').fill('*a')
    await page.getByRole('button', { name: 'Luo DFA' }).click()
    await expect(page.getByText('Virheellinen ensimmäinen tai viimeinen merkki.')).toBeVisible()
    await expect(page.getByText('Syötä säännöllinen lauseke:')).toBeVisible()
    await expect(page.getByRole('button', { name: 'Näytä kuva' })).not.toBeVisible()

  })

  test('error notification is rendered after input with invalid last symbol', async ({page}) => {
    await page.goto('http://localhost:5173')
    await page.getByRole('textbox').fill('a|')
    await page.getByRole('button', { name: 'Luo DFA' }).click()
    await expect(page.getByText('Virheellinen ensimmäinen tai viimeinen merkki.')).toBeVisible()
    await expect(page.getByText('Syötä säännöllinen lauseke:')).toBeVisible()
    await expect(page.getByRole('button', { name: 'Näytä kuva' })).not.toBeVisible()

  })

  test('error notification is rendered after input with invalid star operation use', async ({page}) => {
    await page.goto('http://localhost:5173')
    await page.getByRole('textbox').fill('a**')
    await page.getByRole('button', { name: 'Luo DFA' }).click()
    await expect(page.getByText('Virheellinen tähtioperaation käyttö.')).toBeVisible()
    await expect(page.getByText('Syötä säännöllinen lauseke:')).toBeVisible()
    await expect(page.getByRole('button', { name: 'Näytä kuva' })).not.toBeVisible()

  })

  test('error notification is rendered after input with invalid union operation use', async ({page}) => {
    await page.goto('http://localhost:5173')
    await page.getByRole('textbox').fill('a||b')
    await page.getByRole('button', { name: 'Luo DFA' }).click()
    await expect(page.getByText('Virheellinen yhdisteoperaation käyttö.')).toBeVisible()
    await expect(page.getByText('Syötä säännöllinen lauseke:')).toBeVisible()
    await expect(page.getByRole('button', { name: 'Näytä kuva' })).not.toBeVisible()

  })

})

