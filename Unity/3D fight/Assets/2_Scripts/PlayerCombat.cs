using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerCombat : MonoBehaviour
{
    public float hp;
    public Weapon curWeapon;

    private void Reset()
    {
        curWeapon = GetComponentInChildren<Weapon>();
    }

    private void Awake()
    {
        curWeapon = GetComponentInChildren<Weapon>();
        curWeapon.owner = this;
    }

 

    public void Attack()
    {
        
    }

    public void Damaged(Damaged damage)
    {
        Debug.Log($"{damage.attacker.name}가 {damage.attackPower}의 데미지를 입혔음");
    }

    public void CanDamagedTarget()
    {
        curWeapon.Enable(true);
    }

    public void CantDamagedTarget()
    {
        curWeapon.Enable(false);
    }
}
