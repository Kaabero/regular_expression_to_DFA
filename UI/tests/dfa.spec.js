import { test, expect} from '@playwright/test'
import { describe } from 'node:test'



describe('DFA', () => {
  
  test('after valid input dfa information is renered', async ({page}) => {
    await page.goto('http://localhost:5173')
    await page.getByRole('textbox').fill('(a|b)*abb')
    await page.getByRole('button', { name: 'Luo DFA' }).click()
    await expect(page.getByText('Säännöllisen lausekkeen "(a|b)*abb" DFA:')).toBeVisible()
    await expect(page.getByRole('button', { name: 'Näytä kuva' })).toBeVisible()
    await expect(page.getByRole('button', { name: 'Näytä tiedot' })).not.toBeVisible()
    await expect(page.getByRole('button', { name: 'Aloita alusta' })).toBeVisible()
    await expect(page.getByText('Tilat: {1, 2, 3, 4}')).toBeVisible()
    await expect(page.getByText('Aakkosto: {a, b}')).toBeVisible()
    await expect(page.getByText('Siirtymät:')).toBeVisible()
    await expect(page.getByText('Alkutila: 1')).toBeVisible()
    await expect(page.getByText('δ(2, b)=3')).toBeVisible()
    await expect(page.getByText('Hyväksyvät tilat: {4}')).toBeVisible()


  })

  test('after input with only € symbol dfa information is renered without transitions', async ({page}) => {
    await page.goto('http://localhost:5173')
    await page.getByRole('textbox').fill('€')
    await page.getByRole('button', { name: 'Luo DFA' }).click()
    await expect(page.getByText('Säännöllisen lausekkeen "€" DFA:')).toBeVisible()
    await expect(page.getByText('Tilat: {1}')).toBeVisible()
    await expect(page.getByText('Tyhjä aakkosto')).toBeVisible()
    await expect(page.getByText('Siirtymät:')).toBeVisible()
    await expect(page.getByText('Alkutila: 1')).toBeVisible()
    await expect(page.getByText('Ei siirtymiä')).toBeVisible()
    await expect(page.getByText('Hyväksyvät tilat: {1}')).toBeVisible()


  })
  
})

