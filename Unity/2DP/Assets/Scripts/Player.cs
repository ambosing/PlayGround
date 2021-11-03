using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player : MonoBehaviour
{
    public float dieYPos = -20f;
    public bool isDead = false;
    private Rigidbody2D _rigidbody2D;
    private Animator _animator;

    private void Awake()
    {
        _rigidbody2D = GetComponent<Rigidbody2D>();
        _animator = GetComponent<Animator>();
    }

    private void Update()
    {
        if (transform.position.y <= dieYPos && !isDead)
        {
            Die();
        }
    }

    // Die애니메이션 -> Idle로 넘겨주기
    private IEnumerator DieCoroutine()
    {
        Debug.Log("사망");
        isDead = true;
        _animator.SetTrigger("Die");



        yield return new WaitUntil(() => _animator.
            GetCurrentAnimatorStateInfo(0).IsName("Dying"));
        //length : 애니메이션 시간
        //yield return new WaitForSeconds(_animator.
        //                                GetCurrentAnimatorStateInfo(0).
        //                                length);

        isDead = false;
        //nomalizedTime은 0~1사이로 정규화한 플레이 퍼센트라고 생각
        //nomalizedTime을 쓰는게 좋다. 왜냐하면 애니메이션을 동기적으로 실행하지 않음.
        //그렇기에 length로 구현하는 것은 애니메이션 상태를 가져와야 하는 추가적인 작업이 필요하게 됨
        // 그래서 오히려 nomalizedTime이 필요하다.

        yield return new WaitUntil(() =>
                                    _animator.
                                    GetCurrentAnimatorStateInfo(0).
                                    normalizedTime >= 0.8f);
        Debug.Log("사망 애니메이션 끝!");

        //1.
        //_animator.SetTrigger("Respawn");
        //2.
        _animator.Play("Idle", -1, 0f);
        //3.

        _rigidbody2D.velocity = Vector2.zero;
        transform.position = GameManager.Instance.spawnPoints.curSpawnPoint.transform.position;

        isDead = false;
    }

    public void Die()
    {
        if (isDead)
            return;
        StartCoroutine(DieCoroutine());
        
    }
}
